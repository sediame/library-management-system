from src.cabin import Cabin
from typing import Set
from src.article import Article
from src.user import User


class Library:
    def __init__(self, name: str):
        self.store: Set[Article] = set()
        self.subscribers = set()
        self.track_book = dict()
        self.name = name
        # self.cabin = Cabin()

    def add_article(self, a: Article):
        self.store.add(a)
        print(type(a))

    def addition(self, key, value):
        self.track_book[key] = value

    def remove_article(self, isbn: str) -> bool:
        if len(self.store) == 0:
            print("your store is empty")
            return True
        for a in self.store:
            if a.isbn == isbn:
                self.store.remove(a)
                print("your book has been deleted")
                return True
        print("You book has not been found")
        return False

    def list_article(self) -> None:
        print(self.store)

    def search(self, isbn: str) -> bool:
        for art in self.store:
            if isbn == art.isbn:
                print("your book has been founded")
                return True
        print("your book has not been founded")
        return False

    def borrow(self, isbn: str, user_id: str) -> bool:
        for art in self.store:
            if (isbn == art.isbn) and art.accessible:
                print("your book has been found and you can borrow it")
                self.addition(isbn, user_id)
                print(self.track_book)
                art.accessible = False
                return True
        print("sorry, book is not available")
        return False

    def add_user(self, a: User):
        self.subscribers.add(a)
        print(type(a))

    def list_user(self) -> None:
        print(self.subscribers)