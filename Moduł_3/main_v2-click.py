import click
from datetime import datetime
from database import DataBaseController


@click.command()
@click.option('--count', help='Number of greetings.')
def create_db(count):
    for x in range(count):
        click.echo(f"Creating DB!")


@click.command()
@click.option('--show-books')
def show_books():
    dbc = DataBaseController()
    all_lent_books = dbc.get_all()
    for lent_book in all_lent_books:
        print(f"""
        \tID: {lent_book.id},
        \tEmail: {lent_book.email}, 
        \tName: {lent_book.name}, 
        \tBook Title: {lent_book.book_title}, 
        \tLent At: {lent_book.lent_at}
        \tReturn At: {lent_book.return_at}"""
              )


if __name__ == '__main__':
    create_db()
    show_books()

still working on ....
