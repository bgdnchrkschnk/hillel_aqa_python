from faker import Faker
fake = Faker()
from random import choice


def get_users_create_payload():
    data: dict = {
        "name":fake.name(),
        "gender":choice(["male", "female"]),
        "email":fake.email(),
        "status":"active"
    }
    return data


print(get_users_create_payload())