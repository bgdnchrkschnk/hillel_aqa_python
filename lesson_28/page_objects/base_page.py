from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from lesson_28.locators.base_page import BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    @property
    def sing_up_login_button(self):
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.SING_UP_LOGIN_BUTTON.value))

    @property
    def logout_page(self):
        return self.wait.until(EC.element_to_be_clickable(BasePageLocators.LOGOUT_BUTTON.value))


    def navigate_to_signup_login_page(self):
        from lesson_28.page_objects.signup_login_page import SignupLoginPage
        self.sing_up_login_button.click()
        return SignupLoginPage(self.driver)

