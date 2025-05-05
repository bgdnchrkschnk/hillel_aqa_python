# class Animal:
#     ...
from abc import abstractmethod


class Animal:

    head: int = 1 # attribute of class
    eyes: int = 2
    paws: int = 4

    def __init__(self, name: str, color: str, is_alive: bool = True):
        self.name = name # attribute of instance of class
        self.color = color
        self.is_alive = is_alive
        self.age = 5

    def speak(self): # methods of instance of class
        pass








