class Event:
    def __init__(self, name, date, address, description, preacher):
        self.name = name
        self.date = date
        self.address = address
        self.description = description
        self.preacher = preacher

class User:
    def __init__(self, name, date_birth, email, phone, address):
        self.name = name
        self.date_birth = date_birth
        self.email = email
        self.phone = phone
        self.address = address