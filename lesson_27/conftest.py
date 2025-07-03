import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="session")
def joom_driver_implicit(request):
    driver_obj = webdriver.Chrome()
    driver_obj.maximize_window()
    driver_obj.implicitly_wait(time_to_wait=20)

    yield driver_obj


@pytest.fixture(scope="session")
def joom_driver(request):
    driver_obj = webdriver.Chrome()
    driver_obj.maximize_window()

    yield driver_obj

# def wait_element():
#     yield WebDriverWait()