from datetime import datetime

import click
from database import DataBaseController
from mailing import EmailSenderManager


@click.group()
def cli():
    pass


@cli.command(help='Initialize new database in current directory.')
def create_db():
    dbc = DataBaseController()
    dbc.create_db()
    click.echo('create-db')


@cli.command(help='Adds one book to database. When launched follow the prompts')
def add_book():
    dbc = DataBaseController()
    click.echo('Provide information')
    email = input('email: ')
    name = input('name: ')
    book_title = input('book_title: ')
    return_at = input('return_at [yyyy-mm-dd]: ')
    dbc.add_book(email, name, book_title, return_at)


@cli.command(help='Shows all books depending on given query')
@click.option('--param', '-p',
              type=str,
              help='Shows all lent books for given one param: name, email, book_title, lent_at, return_at',
              prompt='keys: (name, email, book_title, lent_at, return_at)\nexample: name=value1\n',
              required=True)
def show_all_by(param: str):
    dbc = DataBaseController()
    all_books = dbc.get_by_query(param)
    for lent_book in all_books:
        click.echo(
            f"""
            ID: {lent_book.id},
            Email: {lent_book.email},
            Name: {lent_book.name},
            Book Title: {lent_book.book_title},
            Lent At: {lent_book.lent_at}
            Return At: {lent_book.return_at}"""
        )


@cli.command(help='Shows all lent books')
def show_books():
    dbc = DataBaseController()
    all_lent_books = dbc.get_all()
    for lent_book in all_lent_books:
        click.echo(
            f"""
            ID: {lent_book.id},
            Email: {lent_book.email}, 
            Name: {lent_book.name}, 
            Book Title: {lent_book.book_title}, 
            Lent At: {lent_book.lent_at}
            Return At: {lent_book.return_at}"""
        )


@cli.command(help='Clears database content')
def clear():
    click.echo('clear!')


@cli.command(help='Updates record with given ID to given values as kwargs')
@click.argument('record_id')
@click.option('--param', '-p',
              required=True,
              prompt='Example kwargs: return_at=2020-02-20')
def update_by_id(record_id, param):
    click.echo(f'the_id: {record_id}')
    click.echo(f'param: {param}')
    dbc = DataBaseController()
    dbc.update_db_by_id_with_query(record_id, param)


@cli.command(help='Check if date to return book is today and sends reminder via email')
def check_and_send():
    dbc = DataBaseController()
    today = datetime.today().date()
    receivers = dbc.check_when_event_day(today)
    print('receivers: ', receivers)
    with EmailSenderManager(ssl_enable=True) as manager:
        for receiver in receivers:
            msg = manager.create_message(
                receiver.name,
                receiver.email,
                receiver.book_title,
                receiver.lent_date
            )

            print(receiver.lent_date)
            manager.send_mail(receiver, msg)


if __name__ == '__main__':
    cli()
