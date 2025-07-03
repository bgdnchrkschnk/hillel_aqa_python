from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.python_site.base_page import BasePage
from page_objects.python_site.signup_validation_page import SignupValidationPage


class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def email_field(self):
        return self.wait.until(EC.visibility_of_element_located(((By.ID, "id_email"))))

    @property
    def username_field(self):
        return self.wait.until(EC.visibility_of_element_located(((By.ID, "id_username"))))

    @property
    def password_field(self):
        return self.wait.until(EC.visibility_of_element_located(((By.ID, "id_password1"))))

    @property
    def password_confirmation_field(self):
        return self.wait.until(EC.visibility_of_element_located(((By.ID, "id_password2"))))

    @property
    def submit_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign Up')]")))

    def enter_email(self, email):
        self.email_field.send_keys(email)

        return self

    def enter_username(self, username):
        self.username_field.send_keys(username)

        return self

    def enter_password(self, password):
        self.password_field.send_keys(password)

        return self

    def confirm_password(self, password):
        self.password_confirmation_field.send_keys(password)

        return self

    def submit_registration(self):

        self.submit_button.click()

        return SignupValidationPage(self.driver)