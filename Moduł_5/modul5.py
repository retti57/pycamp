from argparse import Namespace, ArgumentParser, Action, ArgumentError, RawTextHelpFormatter
import getpass
from typing import Any, Sequence


class Password(Action):
    def __call__(self, parser: ArgumentParser, namespace: Namespace, values, option_string) -> None:
        values: Sequence[Any] | Any | bool
        if values in None:
            values = getpass.getpass('Enter password: ')

        setattr(namespace, self.dest, values)


def filename(value: str):
    if value.endswith('.txt'):
        return value
    raise ArgumentError(None, 'Wrong file extension')


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
    help='Sets talkative level'
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
group.add_argument('-f', '--file', action='append', type=filename, help='List of files to process.')
group.add_argument('-d', '--dir', help='Path to folder with files to process.')


args = arg_parser.parse_args()
print(args)
