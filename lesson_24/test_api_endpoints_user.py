import pytest
import requests

# Фабрика для створення об'єктів "користувач"
class UsersFactory:
    @staticmethod
    def create_user(name, email):
        return {"name": name, "email": email}

# Тести для REST API з використанням фабрики та параметризації
@pytest.fixture
def base_url():
    return "http://127.0.0.1:7070/users"

@pytest.mark.parametrize("url", ["/1", "/2"])
def test_get_user(base_url, url):
    final_endpoint = base_url + url
    response = requests.get(final_endpoint)
    assert response.status_code == 200
    user_data = response.json()
    assert "name" in user_data
    assert "email" in user_data

@pytest.mark.parametrize("url", ["/create"])
def test_create_user(base_url, url):
    user_data = UsersFactory.create_user("John Doe", "john.doe@example.com")
    final_endpoint = base_url + url
    response = requests.post(final_endpoint, json=user_data)
    assert response.status_code == 201
    user_id = response.json()["id"]
    assert user_id is not None

@pytest.mark.parametrize("url", ["/delete/1", "/delete/2"])
def test_delete_user(base_url, url):
    final_endpoint = base_url + url
    response = requests.delete(final_endpoint)
    assert response.status_code == 204