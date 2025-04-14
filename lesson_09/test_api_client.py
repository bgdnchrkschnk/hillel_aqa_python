import unittest
from unittest.mock import patch, Mock
from api_client import APIClient


class TestAPIClient(unittest.TestCase):

    @patch('requests.get')
    def test_api_mock_response(self, mock_get):
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {"message": "OK"}
        mock_get.return_value = mock

        api_client = APIClient("https://api.example.com")
        result = api_client.get_data()

        mock_get.assert_called_once_with('https://api.example.com/data')

        # Перевіряємо результат
        assert {"message": "OK"} == result


    @patch('requests.get')
    def test_api_mock_response(self, mock_get):
        mock = Mock()
        mock.status_code = 400
        mock.json.return_value = {"message": "failed"}
        mock_get.return_value = mock

        api_client = APIClient("https://api.example.com")
        result = api_client.get_data()

        mock_get.assert_called_once_with('https://api.example.com/data')

        # Перевіряємо результат
        assert {"message": "OK"} == result

