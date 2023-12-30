from os import walk
import pathlib, getpass, argparse
from argparse import Namespace, ArgumentParser,  RawTextHelpFormatter
from time import time, sleep
from typing import Any, Sequence
from tqdm import tqdm
from crypto import Encryption, Decryption, Append
from cryptography.fernet import InvalidToken


class Password(argparse.Action):
    def __call__(self, parser: ArgumentParser, namespace: Namespace, values: Sequence[Any] | str | None, option_string) -> None:
        if values is None:
            values = getpass.getpass('Enter password: ')

        setattr(namespace, self.dest, values)


def filename_validator(value: str):
    if value.endswith(('.txt', '.dokodu')):
        return value
    raise argparse.ArgumentError(None, 'Wrong file extension')


def list_files_in_directory(dirname: str):
    files_to_return = []

    for path, dirs, files in walk(dirname):
        for file in files:
            files_to_return.append(f'{path}\\{file}')

    return files_to_return


def main(args: Namespace):
    try:
        if args.dir:
            files_to_process = list_files_in_directory(args.dir)
        elif args.file:
            files_to_process = args.file
        else:
            raise argparse.ArgumentError(argument=None, message='wrong argument')

        if args.verbose >= 3:
            files_to_process = tqdm(files_to_process)

        for file in files_to_process:
            sleep(.2)
            before = time()
            path = pathlib.Path(file)
            if args.mode == 'encrypt':
                action = Encryption(path)
            elif args.mode == 'decrypt':
                action = Decryption(path)
            elif args.mode == 'append':
                text = input('\nWhat to append?: ')
                action = Append(path, text)
            action.execute(args.password)
            after = time()
            if 0 < args.verbose <= 2:
                print(file, end=' ')
                if args.verbose > 1:
                    print(after-before)
                print()

            if args.verbose >= 3:
                files_to_process.set_description(file)

    except InvalidToken:
        print('Invalid password')
    except argparse.ArgumentError as err:
        print(err)


if __name__ == "__main__":
    arg_parser = ArgumentParser(description='Decrypt encrypt app', formatter_class=RawTextHelpFormatter)
    arg_parser.add_argument(
        '-m', '--mode',
        choices=['encrypt', 'decrypt', 'append'],
        required=True,
        help='''encrypt -> file encryption
    decrypt -> file decryption
    append -> append text to encrypted file'''
    )
    arg_parser.add_argument(
        '-v', '--verbose',
        action='count',
        default=0,
        help='Sets talkativity level'
    )
    arg_parser.add_argument(
        '-p', '--password',
        required=True,
        help='Enter password',
        nargs='?',
        dest='password',
        action=Password
    )

    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', action='append', type=filename_validator, help='List of files to process.')
    group.add_argument('-d', '--dir', help='Path to folder with files to process.')

    args = arg_parser.parse_args()

    main(args)
