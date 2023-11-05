from sys import argv
from sqlalchemy import create_engine, Column, Integer, String, select, Date, delete
# from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, date

# tożsame:
# with sqlite3.connect('books.db') as connection:
# cursor = connection.cursor()
# cursor.execute()
# connection.commit()

engine = create_engine('sqlite:///lent_books.db')

Base = declarative_base()  # model klasy obieków


class LentBook(Base):
    __tablename__ = 'lent_books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False)
    name = Column(String, nullable=False)
    book_title = Column(String, nullable=False)
    lent_at = Column(Date, nullable=False, default=date.today())
    # lent_at = Column(Date, nullable=False, default=func.now())
    return_at = Column(Date, nullable=False)


def create_db():
    Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)


def add_book(email_address: str, name_who_lent_book: str, borrowed_book_title: str, to_be_return_at: str):
    session = Session()
    return_date = datetime.strptime(to_be_return_at, "%Y-%m-%d").date()
    new_lent_book = LentBook(
        email=email_address,
        name=name_who_lent_book,
        book_title=borrowed_book_title,
        return_at=return_date
    )
    session.add(new_lent_book)
    session.commit()


def show_all():
    session = Session()
    # Przykład pobrania wszystkich rekordów
    all_lent_books = session.query(LentBook).all()
    for lent_book in all_lent_books:
        print(f"""
            ID: {lent_book.id}, 
            Email: {lent_book.email}, 
            Name: {lent_book.name}, 
            Book Title: {lent_book.book_title}, 
            Lent At: {lent_book.lent_at.date()}
            Return At: {lent_book.return_at.date()}""")


def date_check():
    today = datetime.today().date()
    session = Session()

    # Przykład pobrania wszystkich rekordów

    books_to_return = session.execute(
        select(LentBook).where(LentBook.return_at <= today))

    for lent_book in books_to_return.scalars():

        print(f"""
                Who lent book: {lent_book.name}
                Email: {lent_book.email},
                Book Title: {lent_book.book_title},
                Return At: {lent_book.return_at.date()}""")


def clear_db():
    session = Session()
    for book in session.execute(select(LentBook)).all():
        stmt = delete(book)
        session.execute(stmt)
    session.commit()


if __name__ == '__main__':
    if len(argv) == 2 and argv[1] == 'create-db':
        create_db()
    elif len(argv) == 2 and argv[1] == 'add-book':
        email = input('email: ')
        name = input('name: ')
        book_title = input('book_title: ')
        return_at = input('return_at [yyyy-mm-dd]: ')
        add_book(email, name, book_title, return_at)
    elif len(argv) == 2 and argv[1] == 'show-books':
        show_all()
    elif len(argv) == 2 and argv[1] == 'clear':
        clear_db()
    else:
        date_check()


