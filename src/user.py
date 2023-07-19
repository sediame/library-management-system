class User:
    def __init__(self, unique_id=0, name=None, last_name=None, sex=None, birthday=None, date_registration=None):
        self.unique_id = unique_id
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.birthday = birthday
        self.date_registration = date_registration

    def __repr__(self):
        return f"(id:{self.unique_id}, name = {self.name}, date of registration = {self.date_registration})"
