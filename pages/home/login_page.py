from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import  logging


class LoginPage(SeleniumDriver):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    # Locators
    _email_field="identifierId"
    _password_field="//div[@id='password']/div[1]/div/div[1]/input"
    _next_button="identifierNext"
    _login_button="//div[@id='passwordNext']/span/span"
    _inbox_link="Inbox"
    _invalid_login_error="//div[@class='o6cuMc']"

    def click_next_button(self):
        self.wait_for_element(self._next_button)
        self.element_click(self._next_button)

    def click_login_button(self):
        self.wait_for_element(self._login_button, locator_type="xpath")
        self.element_click(self._login_button, locator_type="xpath")

    def enter_email(self, email):
        self.wait_for_element(self._email_field)
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.wait_for_element(self._password_field, locator_type="xpath")
        self.send_keys(password, self._password_field, locator_type="xpath")

    def login(self,email="",password=""):
        self.enter_email(email)
        self.click_next_button()
        self.enter_password(password)
        self.click_login_button()

    def verify_login_success(self):
        result=self.is_element_present(self._inbox_link, locator_type="link")
        return result

    def verify_invalid_login(self):
        result=self.is_element_present(self._invalid_login_error, locator_type="xpath")
        return result

    def verify_title(self):
        if self.get_title() == 'Google':
            return True
        else:
            return False
