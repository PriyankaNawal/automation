from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import utilities.custom_logger as cl
import  logging


class InboxPage(SeleniumDriver):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _email_links="div.xS>div.xT>div.y6>span.bog"
    _email_parent="td[class='Bu bAn']"

    def open_email(self):
        mails=self.wait_for_all_elements(self._email_links, locator_type="css")
        for mail in mails:
            mail.find_element_by_tag_name('span').click();
            break

    def verify_subject(self):
        email_parent=self.wait_for_element(self._email_parent, locator_type="css")
        email_subject = email_parent.find_element_by_css_selector("div[class='ha']").find_element_by_tag_name("h2").text
        if email_subject == 'Test subject':
            return True
        else:
            return False
