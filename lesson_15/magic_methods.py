import random


class User():
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age
        self.friends: list[User] = []

    def add_friend(self, user):
        self.friends.append(user)

    # Dunderscore methods (Magic methods)

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return f"{self.name} is {self.age} years old\nFriends: {self.friends}"

    def __repr__(self):
        return f"User obj: {self.name}"

    def __eq__(self, other):
        if not isinstance(other, User):
            raise TypeError(f"{type(other)} is not a User")
        return self.age == other.age and self.friends == other.friends

    def __lt__(self, other):
        """
        Method checks if one user.name is shorter than another
        """
        return len(self.name) < len(other.name)

    def __gt__(self, other):
        return len(self.name) > len(other.name)

    def __call__(self, *args, **kwargs):
        print(f"User {self.name} is called")

    def __contains__(self, item):
        return item in self.friends

    def __setattr__(self, key, value):
        if key == "age" and value <= 0:
            raise ValueError(f"{key} is not a valid age")
        print(f"Setting {key} to {value}")
        super().__setattr__(key, value)


kostya_user: User = User(name="Kostya", age=35)
diana_user: User = User(name="Diana", age=18)
kostya_user.add_friend(diana_user)
kostya_user.mood = "Fine!"
kostya_user.age = 1



setattr(kostya_user, "is_employed", True)
kostya_friends: list[User] = kostya_user.friends

kostya_friends_other_way: list[User] = getattr(kostya_user, "friends")

print(kostya_friends)
print(kostya_friends_other_way)

print(
    getattr(kostya_user, "is_employed")
)




# animal: Animal = Animal(name="animal", color="blue")
#
# print(test_user_one == animal)


# print(callable(kostya))
# kostya()


# class DataProvider:
#
#     def __call__(self, limit, **kwargs) -> dict:
#         res_dict = {"test_data": random.randint(1,limit),
#                     "animal": "animal"
#                     }
#         return res_dict
#
#
# data_provider = DataProvider()
#
# print(data_provider(limit=100))




# print(kostya_user)
# print(diana_user)
#
# print(
#     kostya_user in diana_user
# )

print(len(kostya_user))


