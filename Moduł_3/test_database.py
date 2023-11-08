from sqlalchemy import create_engine
from database import DataBaseController


class DataBase(DataBaseController):

    def __init__(self):
        super().__init__()
        self.engine = create_engine('sqlite://')


class TestDatabase:
    DB = DataBase()
    DB.create_db()

    def test_books_addition_to_db_and_returning_them(self):
        email = 'someone@else'
        name = 'someone'
        book_title = 'Pan Samochodzik'
        return_at = '2023-12-07'
        self.DB.add_book(email, name, book_title, return_at)
        books = self.DB.get_all()
        # print(books)
        assert books[0].email == email
        assert books[0].name == name
        assert books[0].book_title == book_title

        email = 'someone2@else'
        name = 'someone2'
        book_title = 'Pan Samochodzik i limuzyna'
        return_at = '2023-12-10'
        self.DB.add_book(email, name, book_title, return_at)
        books = self.DB.get_all()

        assert len(books) == 2
        assert books[1].book_title == book_title
