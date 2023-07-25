class User:
    def __init__(self, id_user=None, name=None, last_name=None, gender=None, birthday=None, date_registration=None):
        self.id_user = id_user
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday
        self.date_registration = date_registration

    def __repr__(self):
        return f"(id:{self.id_user}, name = {self.name}, date of registration = {self.date_registration})"
