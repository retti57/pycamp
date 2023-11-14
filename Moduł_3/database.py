from sqlalchemy import create_engine, Column, Integer, String, select, Date, delete, update
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, date
from collections import namedtuple

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

    def check_when_event_day(self, event_date):
        session = self.create_connection()

        books_to_return = session.execute(
            select(LentBook).where(LentBook.return_at <= event_date)
        )
        books_to_be_returned = books_to_return.scalars()

        receivers = []
        Receiver = namedtuple('Receiver', 'name email lent_book lent_date')
        for lent_book in books_to_be_returned:
            receiver = Receiver(
                lent_book.name,
                lent_book.email,
                lent_book.book_title,
                lent_book.lent_at.strftime('%Y-%m-%d')
            )
            receivers.append(receiver)
            print(f"""
                    Who lent book: {receiver.name}
                    Email: {receiver.email},
                    Book Title: {receiver.lent_book},
                    Lent At: {receiver.lent_date}""")

        return receivers

    def clear_db(self):
        session = self.create_connection()

        for book in session.query(LentBook).all():
            book_id_to_delete = book.id
            stmt = delete(LentBook).where(book.id == book_id_to_delete)
            session.execute(stmt)
        session.commit()

    def update_db_lent_date(self, cond_date, newdate):
        session = self.create_connection()

        stmt = update(LentBook).where(LentBook.lent_at == cond_date).values(lent_at=newdate)
        session.execute(stmt)
        session.commit()

    def update_db_return_date(self, cond_date, newdate):
        session = self.create_connection()

        stmt = update(LentBook).where(LentBook.return_at == cond_date).values(return_at=newdate)
        session.execute(stmt)
        session.commit()
