import os

from lesson_23.base_api_service import BaseApiService
from requests import Response, Session
from dotenv import load_dotenv
load_dotenv()
import logging
logging.basicConfig(level=logging.DEBUG)


class ApiServiceQAuto(BaseApiService):

    BASE_URL: str = 'https://qauto.forstudy.space/api'

    def __init__(self):
        self.session: Session = Session()
        self.session.close()

    def _get(self, final_endpoint: str) -> Response:
        return self.session.get(url=final_endpoint)

    def _post(self, final_endpoint: str, json: dict) -> Response:
        return self.session.post(url=final_endpoint, json=json)

    def _put(self, final_endpoint: str, json: dict) -> Response:
        return self.session.put(url=final_endpoint, json=json)

    def _delete(self, final_endpoint: str) -> Response:
        return self.session.delete(url=final_endpoint)

    def login(self, email: str, password: str, remember: bool = False) -> None:
        request_dict: dict = {'email': email,
                              'password': password,
                              'remember': remember}
        final_endpoint: str = f'{self.BASE_URL}/auth/signin'
        login_response = self._post(final_endpoint=final_endpoint, json=request_dict)
        if login_response.status_code == 200:
            logging.info(f'Login is successfull with email: {email}, password: {password}')
        else:
            logging.error(f'Login failed with code: {login_response.status_code}\nemail: {email}, password: {password}')
            raise AssertionError(f'Login failed with code: {login_response.status_code}\n email: {email}, password: {password}')

    def logout(self) -> None:
        final_endpoint: str = f'{self.BASE_URL}/auth/logout'
        logout_response = self._get(final_endpoint=final_endpoint)
        if logout_response.status_code == 200:
            logging.info(f'Logout is successfull')
        else:
            logging.error(f'Logout failed with code: {logout_response.status_code}')


if __name__ == '__main__':
    api_service = ApiServiceQAuto()

    email = os.getenv("test_user_email")
    password = os.getenv("test_user_password")

    api_service.login(email=email, password=password)

    response = api_service.session.get(url=ApiServiceQAuto.BASE_URL+'/users/current')

    print(response.json())





