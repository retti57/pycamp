import click
from database import DataBaseController


@click.group()
def cli():
    pass


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


if __name__ == '__main__':
    cli()
