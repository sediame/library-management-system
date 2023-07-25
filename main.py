from src.library import Library
from src.article import Article
from src.cabin import Cabin
from fastapi import FastAPI
from src.user import User

app = FastAPI()
lib = Library("Central Library Leipzig")


@app.get("/newuser/")
async def add_user(name, last_name, gender=None, birthday=None):

    user = User(name=name, last_name=last_name, gender=gender, birthday=birthday)
    lib.add_user(user)
    lib.list_user()

    return {"status": f"User with name {name} has been added successfully"}

@app.get("/newubook/")
async def add_article(isbn, title, author, type, publication_date = None, edition = None, number_version=1):

    articles = Article(isbn=isbn, title=title, author=author, type=type, publication_date=publication_date, edition=edition, number_version=number_version )
    lib.add_article(articles)
    lib.list_article()

    return {"status": f"book  with title {title} has been added successfully"}
@app.get("/buildcabin/")
async def build_cabin(cabin_id, type):

    cabin = Cabin(cabin_id= cabin_id, type= type)
    lib.build_cabin(cabin)
    lib.list_cabin()

    return {"status": f"cabin  with id {cabin_id} has been added successfully"}

@app.get("/findbook/")
async def search(isbn):
    lib.search(isbn)

    return {"status": f"book  with id {isbn} has been been found"}

@app.get("/borrowbook/")
async def borrow(isbn, user_id):
    lib.borrow(isbn, user_id)

    return {"status": f"cabin  with id {isbn} has been added successfully"}

@app.get("/returnbook/")
async def bring_back_book(isbn):
    lib.bring_back_book(isbn)

    return {"status": f"book  with id {isbn} has been returned successfully"}

@app.get("/removebook/")
async def remove_article(isbn):
    lib.remove_article(isbn)

    return {"status": f"book  with id {isbn} has been removed successfully"}