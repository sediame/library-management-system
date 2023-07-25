from src.article import Article
from src.user import User
from src.cabin import Cabin
import sqlite3
from datetime import date
import shortuuid


class Library:
    def __init__(self, name: str, ):
        # Database Initialization
        self.__connection = sqlite3.connect("library.db")
        self.__cursor = self.__connection.cursor()
        # Create Tables

        self.__cursor.execute("CREATE TABLE IF NOT EXISTS articles(isbn TEXT PRIMARY KEY, \
                                title TEXT NOT NULL, \
                                author TEXT NOT NULL,\
                                type TEXT NOT NULL,\
                                publication_date date,\
                                edition TEXT NOT NULL,\
                                number_version INT NOT NULL,\
                                user_id TEXT  NULL,\
                                date_borrow date NULL,\
                                accessible TEXT NOT NULL)")

        self.__cursor.execute("CREATE TABLE IF NOT EXISTS user(id_user INTEGER PRIMARY KEY, \
                                        name TEXT  NULL, \
                                        last_name TEXT  NULL,\
                                        gender TEXT  NULL,\
                                        birthday date NULL,\
                                        date_registration date NULL)")

        self.__cursor.execute("CREATE TABLE IF NOT EXISTS cabin(cabin_id TEXT PRIMARY KEY, \
                                                type TEXT NOT NULL)")

        self.__connection.commit()
        self.name = name

    def add_article(self, a: Article):
        accessible = True
        self.__cursor.execute("""INSERT INTO articles(isbn, title, author, type, publication_date, edition, number_version, accessible)
                VALUES (?,?,?,?,?,?,?,?)
                """, (
            a.isbn, a.title, a.author, a.type, a.publication_date, a.edition, a.number_version, accessible))
        self.__connection.commit()
        print('Data entered successfully.')


    def remove_article(self, isbn: int) -> bool:
        self.__cursor.execute(f"DELETE  FROM articles where isbn=?", (isbn,))
        print("your book has been deleted")
        self.__connection.commit()

    def list_article(self) -> None:
        result = self.__cursor.execute("SELECT * FROM articles")
        print(result.fetchall())

    def search(self, isbn: str) -> bool:
        result = self.__cursor.execute("SELECT * FROM articles where isbn=?", (isbn,))
        final = result.fetchall()
        if len(final) != 0:
            if final[0][7] == None:
                location = self.location_book(isbn)
                print(f"Hello, your book has been found in cabin numer  {location} ")
            else:
                print(f"Hello, this book has been borrowed by user  {final[0][7]} ")
        else:
            print("your book has not  been found in library")

    def borrow(self, isbn: int, user_id) -> bool:
        result = self.__cursor.execute("SELECT isbn, accessible FROM articles where isbn=?", (isbn,))
        final = result.fetchall()
        if len(final) != 0 and (final[0][1] == "1"):
            print("your book has been found and you can borrow it")
            date_borrow1 = date.today()
            self.__cursor.execute("Update articles set user_id= ?, date_borrow = ?, accessible= False  WHERE isbn=?", (
                user_id, date_borrow1, isbn,))
            self.__connection.commit()
            print("data has been borrowed")

            return True

        print("sorry book is not available")
        return False

    def add_user(self, a: User):
        id_user = shortuuid.uuid()[:8]
        date_registration = date.today()
        self.__cursor.execute("""INSERT INTO user(id_user, name, last_name, gender, birthday, date_registration)
                        VALUES (?,?,?,?,?,?)
                        """, (id_user, a.name, a.last_name, a.gender, a.birthday, date_registration))
        self.__connection.commit()
        print('Data entered successfully.')

    def list_user(self) -> None:
        result = self.__cursor.execute("SELECT * FROM user")
        print(result.fetchall())

    def build_cabin(self, a: Cabin):
        self.__cursor.execute("""INSERT INTO cabin(cabin_id, type)
                        VALUES (?,?)""", (a.cabin_id, a.type))
        self.__connection.commit()
        print("your cabin is built")

    def list_cabin(self) -> None:
        result = self.__cursor.execute("SELECT * FROM cabin")
        print(result.fetchall())

    def location_book(self, isbn):
        result = self.__cursor.execute("SELECT cabin_id FROM cabin,articles where cabin.type=articles.type and articles.isbn=? ", (
    isbn,))
        locat = result.fetchall()
        location = locat[0][0]
        return location

    def bring_back_book(self, isbn):
        self.__cursor.execute("Update articles set user_id= NULL, date_borrow = NULL, accessible= TRUE  WHERE isbn=?", (
            isbn,))
        self.__connection.commit()
        print("thanks for bringing back this book")
