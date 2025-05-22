import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()
from lesson_19.data_provider.users import get_users_create_payload


class BaseApiClient:

    BASE_URL = os.getenv("base_url_api")

    def __init__(self):
        self.__token = os.getenv("api_token")
        self._session = requests.Session()
        self.__authentificate()

    @property
    def token(self):
        return self.__token

    def __authentificate(self):
        header: dict = {"Authorization": f"Bearer {self.__token}", "Content-Type": "application/json"}
        self._session.headers.update(header)

    def clear_headers(self):
        self._session.headers.clear()
        self._session.headers.update({"Cookie": "application/json"})

    def _get(self, endpoint: str):
        return self._session.get(url=endpoint, timeout=10)

    def _post(self, endpoint: str, data: dict):
        return self._session.post(url=endpoint, json=data, timeout=10)

    def _put(self, endpoint: str, data: dict):
        return self._session.put(url=endpoint, json=data)

    def _delete(self, endpoint: str):
        return self._session.delete(url=endpoint)


class UserApiClient(BaseApiClient):

    EDPOINT: str = f"{BaseApiClient.BASE_URL}/users"

    def create_user(self, data: dict):
        return self._post(endpoint=f"{self.EDPOINT}", data=data)

    def get_user(self, id):
        endpoint: str = f"{self.EDPOINT}/{id}"
        return self._get(endpoint=endpoint)

    def replace_user(self, id, data: dict):
        return self._put(endpoint=f"{self.EDPOINT}/{id}", data=data)




# user_api_client = UserApiClient()
# payload = get_users_create_payload()
# response: Response = user_api_client.create_user(data=payload)
#
# print(response.status_code)
# print(response.text)
# print(response.json()) # json in dict automatically


