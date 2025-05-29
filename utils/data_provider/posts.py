from faker import Faker
fake = Faker()


def get_user_post_create_payload():
    data: dict = {
        "title":fake.city(),
        "body":fake.text()
    }
    return data


if __name__ == '__main__':
    print(get_user_post_create_payload())