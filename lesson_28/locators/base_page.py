from enum import Enum

from selenium.webdriver.common.by import By


class BasePageLocators(Enum):
    SING_UP_LOGIN_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, "a[href='/login']")
    LOGOUT_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, "a[href='/logout']")


