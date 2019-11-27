from selenium import webdriver
import testdata.test_data as td


class WebDriverFactory():
    def __init__(self,browser):
        self.browser=browser

    def get_web_driver_instance(self):
        base_url=td.test_data("url")
        if self.browser=='iexplorer':
            driver=webdriver.Ie()
        elif self.browser=='firefox':
            driver=webdriver.Firefox()
        elif self.browser == 'chrome':
            driver=webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)
        return driver