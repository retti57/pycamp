import pathlib, getpass, argparse
from argparse import Namespace, ArgumentParser,  RawTextHelpFormatter
from typing import Any, Sequence
from crypto import Encryption, Decryption
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


def main(args: Namespace):
    try:
        for file in args.file:
            path = pathlib.Path(file)
            if args.mode == 'encrypt':
                action = Encryption(path)

            elif args.mode == 'decrypt':
                action = Decryption(path)

            action.execute(args.password)
    except InvalidToken:
        print('Invalid password')


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
