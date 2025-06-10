import random
import sys

from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker

from fixtures.db_client import db_client
from lesson_22.declarative_base import Base
from lesson_22.data_provider.user import get_user
from lesson_22.employee_department import Employee, Department
from lesson_22.user import User
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.DEBUG)
import os
load_dotenv()


class SQLAlchemyClient:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__engine = self.__create_engine()
        self.__session = self.__create_session()

    @property
    def session(self):
        return self.__session

    def __create_engine(self):
        logging.info(f"Creating engine for {self.db_url}...")
        return create_engine(self.db_url)

    def __create_session(self):
        logging.info(f"Creating session for {self.db_url}...")
        session = sessionmaker(bind=self.__engine)
        return session()

    def create_table(self, table_obj):
        logging.info(f"Creating table {table_obj.__tablename__}...")
        table_obj.metadata.create_all(self.__engine)

    def close_connection(self):
        logging.info("Connection closed")
        self.__session.close()
        # self._engine.dispose()

    # def __del__(self):
    #     logging.info("Connection closed")
    #     self.__session.close()
    #     # self._engine.dispose()


if __name__ == '__main__':
    # initialize sqlalchemy_client class
    db_client: SQLAlchemyClient = SQLAlchemyClient(os.getenv("db_url"))

    # creating a table
    db_client.create_table(table_obj=User)
    db_client.create_table(table_obj=Employee)
    db_client.create_table(table_obj=Department)

    # Inserting a user
    # new_user_dict: dict = get_user()
    # new_user: User = User(**new_user_dict) # -> User(name=new_user_dict['name'], age=new_user_dict['age'])

    # db_client.session.add(new_user)
    # db_client.session.commit()

    # Updating one record
    # user = db_client.session.query(User).filter_by(id=2).first() # WHERE name=John
    # user.age = 18
    # db_client.session.commit()

    # Updating several records
    # users = db_client.session.query(User).filter_by(age=18).all() # # Відповідає UPDATE user SET age=19 WHERE age=18;
    #
    # for user in users:
    #     user.age = 19
    #
    # db_client.session.commit()

    # Deleting all users
    # all_users = db_client.session.query(User).all()
    # for user in all_users:
    #     db_client.session.delete(user)
    #
    # db_client.session.commit()

    # for i in range(10):
    #     new_user_dict = get_user()
    #     user = User(**new_user_dict)
    #     db_client.session.add(user)
    #
    # db_client.session.commit()

    # new_users = []
    # for i in range(10):
    #     new_user_dict = get_user()
    #     user = User(**new_user_dict)
    #     new_users.append(user)
    #
    # db_client.session.add_all(new_users)
    # db_client.session.commit()

    # Використання виразів для складного запиту: обчислення середнього віку користувачів
    average_age = int(db_client.session.query(func.avg(User.age)).scalar())
    print("Середній вік користувачів:", average_age)
    # SQL аналог: SELECT AVG(age) FROM users;

    # Використання виразів для складного запиту: підрахунок кількості користувачів
    user_count = int(db_client.session.query(func.count(User.id)).scalar())
    print("Кількість користувачів:", user_count)
    # SQL аналог: SELECT COUNT(id) FROM users;

    it_department: Department = Department(name="IT")
    # db_client.session.add(new_department)
    # db_client.session.commit()

    hr_department = Department(name='HR')
    # db_client.session.add(hr_department)
    # db_client.session.commit()

    john = Employee(name='Bob', department_id=random.choice([1,3]))
    # db_client.session.add(john)
    # alice = Employee(name='Alice', department=hr_department)
    # bob = Employee(name='Bob', department=it_department)

    # session.add_all([it_department, hr_department, john, alice, bob])
    # db_client.session.commit()

    try:
        # Початок транзакції
        db_client.session.close()
        db_client.session.begin()

        # Збільшення ціни для конкретного продукту на 5%
        bob = db_client.session.query(Employee).filter_by(name='Bob').first()
        bob.name = 'Bohdan'

        # Додавання нового продукту
        db_client.session.add(it_department)

        # Підтвердження транзакції
        db_client.session.commit()
    except:
        # Скасування транзакції в разі виникнення помилки
        db_client.session.rollback()
        logging.error(f"Transaction has failed: {sys.exc_info()[0]}")
    finally:
        # Закриття сесії
        db_client.session.


    db_client.close_connection()
