import pytest
from requests import Response

from lesson_19.api_client import UserApiClient
from lesson_19.data_provider.users import get_users_create_payload
from lesson_19.data_models.response_user import User
from pydantic import ValidationError

class TestUsers:

    user_api_client = UserApiClient()

    def test_user_creation_is_successful(self):
        payload_dict = get_users_create_payload()
        response: Response = self.user_api_client.create_user(data=payload_dict)
        response_dict: dict = response.json()
        # assert response.status_code in (201, 204, 200)
        assert response.ok # (201,200, 204)
        assert response_dict.get("id") is not None, f"id was not returned"
        self.user_api_client.current_user_id = response_dict.get("id")

    def test_get_user_by_id_is_successful(self):
        # Creating a user like a precondition
        response: Response = self.user_api_client.create_user(data=get_users_create_payload())
        # Getting user by id
        response: Response = self.user_api_client.get_user(id=response.json().get("id"))
        print(response.json())
        assert response.ok
        keys = [key for key in get_users_create_payload().keys()]
        keys.append("id")

        try:
            User.model_validate(response.json())
        except ValidationError as e:
            print(f"Validation schema has been failed {e}")

        # for key in keys:
        #     print(f"Validating key {key}..")
        #     assert key in response.json(), f"{key} was not returned"

    def test_replace_user_by_id_is_successful(self):
        payload_dict = get_users_create_payload()
        response: Response = self.user_api_client.replace_user(id=self.user_api_client.current_user_id, data=payload_dict)
        assert response.ok

        try:
            User.model_validate(response.json())
        except ValidationError as e:
            print(f"Validation schema has been failed {e}")

        for key, value in payload_dict.items():
            assert response.json().get(key) == value

