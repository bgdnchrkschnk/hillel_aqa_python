import os
import random

import pytest

from lesson_23.api_service_qauto import ApiServiceQAuto
from faker import Faker
fake = Faker()
from dotenv import load_dotenv
load_dotenv()


class TestQAAuto:

    api_service_qauto: ApiServiceQAuto = ApiServiceQAuto()
    email = os.getenv("test_user_email")
    password = os.getenv("test_user_password")

    def test_qa_auto_login_get_userdata_and_logout(self):
        try:
            print(self.email, self.password)
            self.api_service_qauto.login(email=self.email, password=self.password)

            # get user data
            response = self.api_service_qauto.session.get(url=ApiServiceQAuto.BASE_URL + '/users/current')

            # validating response
            assert response.status_code == 200
            assert response.json().get('status') == "ok"

            # update user data
            user_update_body = {
        "photo": "hillel_user.png",
        "name": "hillel_user",
        "lastName": fake.last_name(),
        "dateBirth": f"2021-03-11",
        "country": fake.country(),
    }
            print(user_update_body)
            response = self.api_service_qauto.session.put(url=ApiServiceQAuto.BASE_URL + '/users/profile', json=user_update_body)

            assert response.status_code == 200
            assert response.json().get('status') == "ok"
            assert response.json()['data']['name'] == "hillel_user"

        finally:
            self.api_service_qauto.logout()




