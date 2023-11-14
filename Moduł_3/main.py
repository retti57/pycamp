from datetime import datetime
from sys import argv
from database import DataBaseController
from mailing import EmailSenderManager

if __name__ == '__main__':
    if len(argv) == 2 and argv[1] == 'create-db':
        dbc = DataBaseController()
        dbc.create_db()

    elif len(argv) == 2 and argv[1] == 'add-book':
        dbc = DataBaseController()
        email = input('email: ')
        name = input('name: ')
        book_title = input('book_title: ')
        return_at = input('return_at [yyyy-mm-dd]: ')
        dbc.add_book(email, name, book_title, return_at)

    elif len(argv) == 2 and argv[1] == 'show-books':
        dbc = DataBaseController()
        all_lent_books = dbc.get_all()
        for lent_book in all_lent_books:
            print(f"""
                ID: {lent_book.id}, 
                Email: {lent_book.email}, 
                Name: {lent_book.name}, 
                Book Title: {lent_book.book_title}, 
                Lent At: {lent_book.lent_at}
                Return At: {lent_book.return_at}""")

    elif len(argv) == 2 and argv[1] == 'clear':
        dbc = DataBaseController()
        dbc.clear_db()

    elif len(argv) == 5 and argv[1] == 'update' and argv[2] == 'lent':
        dbc = DataBaseController()
        new_date = datetime.strptime(argv[3], "%Y-%m-%d").date()
        condition_date = datetime.strptime(argv[2], "%Y-%m-%d").date()
        dbc.update_db_lent_date(condition_date, new_date)

    elif len(argv) == 5 and argv[1] == 'update' and argv[2] == 'return':
        dbc = DataBaseController()
        new_date = datetime.strptime(argv[3], "%Y-%m-%d").date()
        condition_date = datetime.strptime(argv[2], "%Y-%m-%d").date()
        dbc.update_db_return_date(condition_date, new_date)

    else:
        dbc = DataBaseController()
        today = datetime.today().date()
        receivers = dbc.check_when_event_day(today)
        print('receivers: ', receivers)
        with EmailSenderManager(ssl_enable=True) as manager:
            for receiver in receivers:
                msg = manager.create_message(
                    receiver.name,
                    receiver.email,
                    receiver.lent_book,
                    receiver.lent_date
                )

                print(receiver.lent_date)
                manager.send_mail(receiver, msg)
