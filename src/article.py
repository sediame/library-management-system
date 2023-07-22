class Article:
    def __init__(self, isbn: str, title=None, author=None, subject=None, publication_date=None, edition=None, number_version=1, accessible=True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.subject = subject
        self.publication_date = publication_date
        self.edition = edition
        self.number_version = number_version
        self.accessible = accessible

    def __repr__(self):
        return f"(isbn:{self.isbn}, title = {self.title}, accessible={self.accessible})"


