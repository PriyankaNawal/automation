import time
from traceback import print_stack
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl
import logging
import time, os


class SeleniumDriver():
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def screenshot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("Exception occurred")
            print_stack()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator Type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found")
        except:
            self.log.info("Element Not Found")
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locator_type)
            print_stack()

    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10):

        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by_type, locator))
            )

            self.log.info("Elements appeared on the web page")
        except:
            self.log.info("Elements not appeared on the web page")
            print_stack()
        return element

    def wait_for_all_elements(self, locator, locator_type="id", timeout=10):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((by_type, locator))
            )

            self.log.info("Elements appeared on the web page")
        except:
            self.log.info("Elements not appeared on the web page")
            print_stack()
        return element
