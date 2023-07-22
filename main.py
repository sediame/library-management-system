
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
        print("Press 8 to list of borrow in library")

        choice = input('Enter your choice: ')

        if choice == "0":
            print("See you later")
            break
        elif choice == "1":
            isbn = lib.id_calcul()+1
            print(isbn)
            title = input('Enter book title: ')
            author = input('Enter book author: ')
            subject = input('Enter book subject: ')
            publication_date = input('Enter book publication_date: ')
            edition = input('Enter book edition: ')
            number_version = input('Enter book number_version: ')
            book = Article(isbn, title, author, subject, publication_date, edition, number_version, True)
            lib.add_article(book)

        elif choice == "2":
            print("list of books:")
            lib.list_article()
        elif choice == "3":
            user_input = input('Enter your isbn for book that you want: ')
            lib.search(user_input)
        elif choice == "4":
            val: int = input('Enter your isbn: ')
            lib.remove_article(val)
        elif choice == "5":
            isbn: str = input('Enter your isbn: ')
            user_id: str = input('Enter your user: ')
            lib.borrow(isbn, user_id)
        elif choice == "6":
            id_user = shortuuid.uuid()[:8]
            name = input('Enter your user name: ')
            last_name = input('Enter your user last name: ')
            gender = input('Enter your user gender (M or F): ')
            birthday = input('Enter your user birthday: ')
            date_registration = date.today()
            user = User(id_user, name, last_name, gender, birthday, date_registration)
            lib.add_user(user)
        elif choice == "7":
            print("list of users:")
            lib.list_user()
        elif choice == "8":
            print("list of borrow:")
            lib.list_borrow()

        else:
            print("I do not know how to perform this yet, Please choose option again")


if __name__ == "__main__":
    main()
