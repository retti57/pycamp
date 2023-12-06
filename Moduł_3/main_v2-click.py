import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='Notifications sender to Borrower',
            usage='Use it for work with data stored in database.\n'
                  'You can either add book, show all of them or delete',
            description='Options to manage with mailing database.'
        )

        self.parser.add_argument(
            '--create-db',
            dest='action',
            action='store_const',
            const='create-db',
            help='creates new database'
        )

        self.parser.add_argument(
            '--add-book',
            dest='action',
            action='store_const',
            const='add-book',
            help='adds book to database'
        )

        self.parser.add_argument(
            '--show-books',
            dest='action',
            action='store_const',
            const='show-books',
            help='shows all information about books stored in database'
        )

        self.parser.add_argument(
            '--clear',
            dest='action',
            action='store_const',
            const='clear-db',
            help='clears database '
        )

        # self.action_group = self.parser.add_mutually_exclusive_group(required=True)


class ExampleParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument(
            '-c','--choice',
            choices=[1, 2],
            type=int
        )
        self.parser.add_argument(
            '-n', '--number',
            action='append',
            help='stores number',
            #
            type=int
        )

        self.second_group = self.parser.add_mutually_exclusive_group(required=False)
        self.second_group.add_argument(
            '-q', '--quiet',
            action='store_true',
            help='getting more quiet'
        )

        self.second_group.add_argument(
            '-v',
            '--verbose',

            help='getting more talkative information',
            action='store_true',
            default=0
        )

    def parse_args(self):
        return self.parser.parse_args()


def pass_validator(value: str):
    if value.startswith('a'):
        raise argparse.ArgumentError
    return value


parser = ExampleParser()

args = parser.parse_args()


print(args)
