from enum import Enum

from selenium.webdriver.common.by import By


class SignupLoginLocators(Enum):
    LOGIN_EMAIL_INPUT: tuple[str, str] = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT: tuple[str, str] = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON: tuple[str, str] = (By.XPATH, "//button[@data-qa='login-button']")