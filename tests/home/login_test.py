from pages.home.login_page import LoginPage
from pages.home.inbox_page import InboxPage
from utilities.teststatus import TestStatus
import testdata.test_data as td
import unittest
import pytest


@pytest.mark.usefixtures("before_class","set_up")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, before_class):
        self.lp = LoginPage(self.driver)
        self.ts= TestStatus(self.driver)
        self.ib=InboxPage(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        self.lp.login(td.test_data("email"), td.test_data("password"))
        result = self.lp.verify_login_success()
        self.ts.mark_final("test_valid_login", result, "Login was successful")

    @pytest.mark.run(order=2)
    def test_open_first_email(self):
        self.ib.open_email()
        result=self.ib.verify_subject()
        self.ts.mark_final("test_open_first_email", result, "Subject verified")