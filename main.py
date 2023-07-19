
from src.library import Library
from src.article import Article
from src.user import User
import shortuuid
from datetime import date


def main():

    lib = Library("Central Library Leipzig")

    while True:
        print("Please choose your option from the list")

        print("Press 0 to exit")
        print("Press 1 to add book")
        print("Press 2 to list of books in library")
        print("Press 3 to search books in library")
        print("Press 4 if you want to remove a book")
        print("Press 5 if you want to borrow a book")
        print("Press 6 if you want to add a user")
        print("Press 7 to list of users in library")

        choice = input('Enter your choice: ')

        if choice == "0":
            print("See you later")
            break
        elif choice == "1":
            isbn = input('Enter your isbn: ')
            book = Article(isbn)
            lib.add_article(book)
        elif choice == "2":
            print("list of books:")
            lib.list_article()
        elif choice == "3":
            user_input = input('Enter your isbn for book that you want: ')
            lib.search(user_input)
        elif choice == "4":
            isbn: str = input('Enter your isbn: ')
            lib.remove_article(isbn)
        elif choice == "5":
            isbn: str = input('Enter your isbn: ')
            user_id: str = input('Enter your user: ')
            lib.borrow(isbn, user_id)
        elif choice == "6":
            user_id = shortuuid.ShortUUID().random(length=6)
            user_name = input('Enter your user name: ')
            date_registration = date.today()
            user = User(unique_id=user_id, name=user_name, date_registration=date_registration)
            lib.add_user(user)
        elif choice == "7":
            print("list of users:")
            lib.list_user()
        else:
            print("I do not know how to perform this yet, Please choose option again")


if __name__ == "__main__":
    main()
