# if you want to make a variable private just use __ example __fullname
from abc import ABC, abstractmethod


class Person:
    first_name: ""
    last_name: ""
    email: ""
    phone_number: ""
    alias: ""
    password: ""


class PersonAbstract(ABC):

    @abstractmethod
    def create_person(self, person: Person):
        pass

    @abstractmethod
    def get_all_persons(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass


class PersonManager(PersonAbstract):
    def create_person(self, person: Person):
        print("Person Information")

    def get_all_persons(self):
        print("Getting all persons")

    def get_user_by_id(self, user_id):
        print("Get one user")


my_person = PersonManager()
my_person.get_all_persons()
