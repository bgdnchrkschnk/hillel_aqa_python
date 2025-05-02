# """
# Inheritence
# Наслідування дозволяє одному класу (підкласу) переймати властивості
# та методи іншого класу (базового).
# """
#
# class Animal:
#     def speak(self):
#         print("Some sound")
#
# class Dog(Animal):
#     pass
#
# dog = Dog()
# dog.speak()  # 👉 "Some sound"
#
#
# """
# Incapsulation
# Приховування внутрішніх деталей реалізації — наприклад,
# через змінні з префіксом _ або __.
# """
#
class Animal:
    def __init__(self, name):
        self.__name = name  # приватна змінна

    def get_name(self):
        return self.__name
#
# cat = Animal("Whiskers")
# print(cat.get_name())  # 👉 "Whiskers"

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__setting_balance_to_0()

    def return_balance(self):
        return self.__balance

    def __setting_balance_to_0(self):
        self.__balance = 0

    def increase_balance(self, amount: float):
        self.__balance = amount


my_account: BankAccount = BankAccount("Bohdan")
my_account.name = "Denys"
print(my_account.name)



# """
# Polymrphism
# Можливість викликати один і той самий метод у різних класах — і він буде працювати по-різному.
# """
#
# class Animal:
#     def speak(self):
#         pass
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow")
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
# animals = [Cat(), Dog()]
# for a in animals:
#     a.speak()  # 👉 Meow, потім Woof
#
#
"""
Abstraction
Описуємо тільки інтерфейс, а не реалізацію. Зручно через abc (abstract base class):
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()  # 👉 Meow
#
# a = Animal()
"""
Метод super() в Python використовується для виклику методів батьківського (базового)
класу з дочірнього (похідного) класу.
Це особливо корисно при наслідуванні, коли потрібно розширити,
а не повністю замінити логіку батьківського класу.
"""