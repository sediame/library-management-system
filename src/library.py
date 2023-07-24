
from src.article import Article
from src.user import User
import sqlite3
from datetime import date


class Library:
    def __init__(self, name: str, ):
        # Database Initialization
        self.__connection = sqlite3.connect("library.db")
        self.__cursor = self.__connection.cursor()
        # Create Tables

        self.__cursor.execute("CREATE TABLE IF NOT EXISTS articles(isbn INTEGER PRIMARY KEY, \
                                title TEXT NOT NULL, \
                                author TEXT NOT NULL,\
                                subject TEXT NOT NULL,\
                                publication_date date,\
                                edition TEXT NOT NULL,\
                                number_version INT NOT NULL,\
                                user_id TEXT  NULL,\
                                date_borrow date,\
                                accessible TEXT NOT NULL)")

        self.__cursor.execute("CREATE TABLE IF NOT EXISTS user(id_user TEXT PRIMARY KEY, \
                                        name TEXT  NULL, \
                                        last_name TEXT  NULL,\
                                        gender TEXT  NULL,\
                                        birthday date NULL,\
                                        date_registration date NULL)")

        self.__cursor.execute("CREATE TABLE IF NOT EXISTS cabin(idCab INTEGER PRIMARY KEY, \
                                                type TEXT NOT NULL, \
                                                first_number_book INTEGER NOT NULL,\
                                                last_number_book INTEGER NOT NULL)")

        self.__connection.commit()
        self.name = name

    def add_article(self, a: Article):
        self.__cursor.execute("""INSERT INTO Articles(isbn, title, author, subject, publication_date, edition, number_version, accessible)
                VALUES (?,?,?,?,?,?,?,?)
                """, (
        a.isbn, a.title, a.author, a.subject, a.publication_date, a.edition, a.number_version, a.accessible))
        self.__connection.commit()
        print('Data entered successfully.')

    def id_calcul(self):
        rows = self.__cursor.execute("SELECT isbn FROM articles ORDER BY isbn DESC LIMIT 1")
        final = rows.fetchall()
        if len(final)==0:
            key = 0
            return key
        else:
            key = final[0][0]
            return key


    def remove_article(self, val: int) -> bool:
        self.__cursor.execute(f"DELETE  FROM articles where isbn={val}")
        print("your book has been deleted")
        self.__connection.commit()

    def list_article(self) -> None:
        result = self.__cursor.execute("SELECT * FROM articles")
        print(result.fetchall())

    def search(self, isbn: int) -> bool:
        result = self.__cursor.execute("SELECT * FROM articles where isbn=?", (isbn))
        final = result.fetchall()
        print(final[0][7])
        if len(final)!=0:
            if final[0][7]==None:
                location = self.location_book(isbn)
                print(f"Hello, your book has been found in cabin numer  {location} ")
            else:
                print(f"Hello, this book has been borrowed by user  {final[0][7]} ")
        else:
            print("your book has not  been found in library")



    def borrow(self, isbn: int, user_idd) -> bool:
        result = self.__cursor.execute("SELECT isbn, accessible FROM articles where isbn=?", (isbn,))
        final = result.fetchall()
        if len(final)!=0  and (final[0][1] == "1"):
            print("your book has been found and you can borrow it")
            date_borrow1 = date.today()
            self.__cursor.execute("Update articles set user_id= ?, date_borrow = ?, accessible= False  WHERE isbn=?", (user_idd, date_borrow1, isbn))
            self.__connection.commit()
            print("data has been insert")

            return True

        print("sorry book is not availible")
        return False



    def add_user(self, a: User):
        self.__cursor.execute("""INSERT INTO user(id_user, name, last_name, gender, birthday, date_registration)
                        VALUES (?,?,?,?,?,?)
                        """, (a.id_user, a.name, a.last_name, a.gender, a.birthday, a.date_registration))
        self.__connection.commit()
        print('Data entered successfully.')

    def list_user(self) -> None:
        result = self.__cursor.execute("SELECT * FROM user")
        print(result.fetchall())
    def insert(self):
        self.__cursor.execute("""INSERT INTO cabin(idCab, type, first_number_book,last_number_book)
                        VALUES (1,"language",1,10),
                               (2,"history",11,20),
                               (3,"math",21,30),
                               (4,"physique",31,40),
                               (5,"informatique",41,50)""")
        self.__connection.commit()
        print("your cabin is built")
    def list_cabin(self) -> None:
        result = self.__cursor.execute("SELECT * FROM cabin")
        print(result.fetchall())
    def location_book(self, isbn):
        result = self.__cursor.execute("SELECT idCab FROM cabin where first_number_book<=? and last_number_book>=?", (isbn, isbn ))
        locat = result.fetchall()
        location = locat[0][0]
        return location

    def bring_back_book(self, isbn):
        self.__cursor.execute("Update articles set user_id= NULL, date_borrow = NULL, accessible= TRUE  WHERE isbn=?", (isbn))
        self.__connection.commit()
        print("thanks for bringing back this book")
