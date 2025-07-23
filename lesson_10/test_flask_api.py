import logging
import requests

from lesson_11.logging_all import logger


content = {'cars': ['Audi, VW', 'Toyota']}
updated_content = {'bikes': ['Honda', 'Suzuki']}


class TestFlaskContent:

    BASE_URL = 'http://127.0.0.1:7070'

    def test_add_content(self):
        logger.info('Checking content adding...')
        logger.info(f"Sending a post request to {self.BASE_URL}/content with body\n{content}'")
        response_data = requests.post(f'{self.BASE_URL}/content', json=content)

        if not response_data.status_code == 200:
            logger.error(f"It wa expected status code 200 but got {response_data.status_code}")
            raise AssertionError(f"It wa expected status code 200 but got {response_data.status_code}")

        if not response_data.json().get('message') == 'Content created successfully!':
            logger.error(f"Unexpected response body message.\nExpected 'Content created successfully!!' but got {response_data.json().get('message')}")
            raise AssertionError(f"Unexpected response body message but got {response_data.json().get('message')}")

    def test_get_content(self):
        logger.info('Getting content...')
        response_get = requests.get(f'{self.BASE_URL}/content')
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content

    def test_modify_content(self):
        logger.info('Modifying content...')
        response = requests.put(f'{self.BASE_URL}/content/0', json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    def test_deleting_content(self):
        logger.info('Deleting content...')
        response = requests.delete(f'{self.BASE_URL}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'