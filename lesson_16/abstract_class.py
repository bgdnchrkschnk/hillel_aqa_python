from abc import ABC, abstractmethod
#
# # Абстрактний клас тварини
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# # Клас собаки, що успадковує абстрактний клас Animal
# class Dog(Animal):
#     def make_sound(self):
#         print("GAV")
#
# # Клас кота, що успадковує абстрактний клас Animal
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
#
# cat = Cat()
# cat.make_sound()
#
# dog = Dog()
# dog.make_sound()


class DbCursor(ABC):
    def __init__(self, db_connector):
        self.conn = db_connector

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def add_user_to_ban_list(self, user_id):
        pass

class PostgresCursor(DbCursor):

    def create_user(self):
        pass

    def get_user_by_id(self, user_id):
        pass

    def add_user_to_ban_list(self, user_id):
        pass

class SQLiteCursor(DbCursor):

    def create_user(self):
        pass
    def get_user_by_id(self, user_id):
        pass
    def add_user_to_ban_list(self, user_id):
        pass

sql_lite = SQLiteCursor(db_connector="conn")
# postgres = PostgresCursor(db_connector="conn")




