import pytest
from selenium import webdriver


@pytest.fixture
def selenium_driver_demo():
    # Ініціалізація веб-драйвера для Chrome
    driver = webdriver.Chrome()

    # # Відкриття веб-сторінки
    driver.get('http://localhost:8000/demo.html')

    yield driver

    # Закриття браузера
    driver.quit()



@pytest.fixture
def selenium_driver_elements():
    # Ініціалізація веб-драйвера для Chrome
    driver = webdriver.Chrome()

    # # Відкриття веб-сторінки
    driver.get('http://localhost:8000/elements.html')

    yield driver

    # Закриття браузера
    driver.quit()

@pytest.fixture
def selenium_driver_scroll():
    # Ініціалізація веб-драйвера для Chrome
    driver = webdriver.Chrome()

    # # Відкриття веб-сторінки
    driver.get('http://localhost:8000/scroll_frame.html')

    yield driver

    # Закриття браузера
    driver.quit()

@pytest.fixture
def selenium_driver_alerts():
    # Ініціалізація веб-драйвера для Chrome
    driver = webdriver.Chrome()

    # # Відкриття веб-сторінки
    driver.get('https://demo.automationtesting.in/Alerts.html')

    yield driver

    # Закриття браузера
    driver.quit()
