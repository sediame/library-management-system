class Article:
    def __init__(self, isbn: str, name=None, title=None, author=None, subject=None, publication_date=None, edition=None, accessible=True):
        self.isbn = isbn
        self.name = name
        self.title = title
        self.author = author
        self.subject = subject
        self.publication_date = publication_date
        self.edition = edition
        self.accessible = accessible

    def __repr__(self):
        return f"(isbn:{self.isbn}, name = {self.name}, accessible={self.accessible})"


