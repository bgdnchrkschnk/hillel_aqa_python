# class User():
#     def __init__(self, name: str, age: int):
#         self.name: str = name
#         self.age: int = age
#         self.__friends: list[User] = []
#
#     def add_friend(self, user):
#         self.__friends.append(user)
#
#     def get_friends(self) -> list:
#         return self.__friends
#
#     # Dunderscore methods (Magic methods)
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old\nFriends: {self.__friends}"
#
#     def __repr__(self):
#         return f"User obj: {self.name}"
#
#     def __eq__(self, other):
#         if not isinstance(other, User):
#             raise TypeError(f"{type(other)} is not a User")
#         return self.age == other.age and self.__friends == other.__friends
#
#     def __lt__(self, other):
#         """
#         Method checks if one user.name is shorter than another
#         """
#         return len(self.name) < len(other.name)
#
#     def __gt__(self, other):
#         return len(self.name) > len(other.name)
#
#     def __call__(self, *args, **kwargs):
#         print(f"User {self.name} is called")
#
#     def __contains__(self, item):
#         return item in self.__friends
#
#     def __setattr__(self, key, value):
#         if key == "age" and value <= 0:
#             raise ValueError(f"{key} is not a valid age")
#         print(f"Setting {key} to {value}")
#         super().__setattr__(key, value)
#
# denis_user: User = User('denis', 25)
#
# # denis_user.__friends.append("denis_user")
#
# print(denis_user.get_friends())
import requests


class BankAccount:
    def __init__(self, username: str, type: str):
        self.username = username
        self.type = type # protected
        self.__balance = 0 # private
        self.__setting_a_new_card()

    def __setting_a_new_card(self): # private
        """
        Method that creates a new card in db
        """
        requests.Request().post(url="test.com/set_new_card", json={"username": self.username, "type": self.type})

    def get_balance(self): # public
        return self.__balance


    def send_money(self, amount, other_user_account):
        self.__balance -= amount
        other_user_account._get_money_from_account(self)







user_account = BankAccount(username="test_user", type="platinum_card")
print(user_account.get_balance())
print(user_account.)

