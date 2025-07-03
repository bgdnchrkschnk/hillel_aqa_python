import pytest
from selenium import webdriver

from lesson_27.page_objects.bing_page_object import BingPageObject


@pytest.fixture
def bing_page():
    chrome_driver = webdriver.Chrome()

    chrome_driver.maximize_window()

    yield BingPageObject(chrome_driver)

    chrome_driver.quit()
