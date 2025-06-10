from faker import Faker
from random import randint
fake = Faker()


def get_user():
    user = {
        "name": fake.name(),
        "age": randint(1, 100),
    }
    return user
