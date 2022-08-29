from collections import UserDict


class AddressBook(UserDict):

    def add_contact(self, name, phone):
        contact = Record(name=name, phone=Phone)
        self.data[name.value] = contact

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones: list[Phone] = [phone] if phone is not None else[]

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def change_phone(self, old_number, new_number):
        try:
            self.phones.remove(old_number)
            self.phones.append(new_number)
        except ValueError:
            return f"{old_number} does not exists"

    def delete_phone(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f"{phone} does not exists"


class Field:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    def __int__(self, phones):
        self.phones: list = phones
