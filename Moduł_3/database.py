from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, select, Date, delete, update
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, date

Base = declarative_base()  # model klasy obieków


class LentBook(Base):
    __tablename__ = 'lent_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
    book_title = Column(String, nullable=False)
    lent_at = Column(Date, nullable=False, default=date.today())
    return_at = Column(Date, nullable=False)


class DataBaseController:

    def __init__(self):
        self.engine = create_engine('sqlite:///lent_books.db')

    def create_connection(self):
        Session = sessionmaker(bind=self.engine)

        return Session()

    def create_db(self):
        Base.metadata.create_all(self.engine)

    def add_book(self, email_address: str, name_who_lent_book: str, borrowed_book_title: str, to_be_return_at: str):
        session = self.create_connection()

        return_date = datetime.strptime(to_be_return_at, "%Y-%m-%d").date()
        new_lent_book = LentBook(
            email=email_address,
            name=name_who_lent_book,
            book_title=borrowed_book_title,
            return_at=return_date
        )
        session.add(new_lent_book)
        session.commit()

    def get_all(self):
        session = self.create_connection()

        return session.query(LentBook).all()

    def date_check(self):
        today = datetime.today().date()
        session = self.create_connection()

        books_to_return = session.execute(
            select(LentBook).where(LentBook.return_at <= today))

        for lent_book in books_to_return.scalars():

            print(f"""
                    Who lent book: {lent_book.name}
                    Email: {lent_book.email},
                    Book Title: {lent_book.book_title},
                    Return At: {lent_book.return_at}""")

    def clear_db(self):
        session = self.create_connection()

        for book in session.query(LentBook).all():
            book_id_to_delete = book.id
            stmt = delete(LentBook).where(book.id == book_id_to_delete)
            session.execute(stmt)
        session.commit()

    def update_db(self, condition_date, new_date):
        session = self.create_connection()

        stmt = update(LentBook).where(LentBook.return_at == condition_date).values(return_at=new_date)
        session.execute(stmt)
        session.commit()


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

    elif len(argv) == 4 and argv[1] == 'update':
        dbc = DataBaseController()
        new_date = datetime.strptime(argv[3], "%Y-%m-%d").date()
        condition_date = datetime.strptime(argv[2], "%Y-%m-%d").date()
        dbc.update_db(condition_date, new_date)

    else:
        dbc = DataBaseController()
        dbc.date_check()




