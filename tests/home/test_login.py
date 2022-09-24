
from pages.home.login_page import LoginPage
from pageActions.home.login_page_actions import LoginPageActions
import unittest
import pytest
import utilities.custom_logger as cs
import logging
import pytest_check as check
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("set_up")
class LoginTests(unittest.TestCase):

    log = cs.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def func_init(self, set_up):
        self.lp = LoginPage(self.driver)
        self.lpa = LoginPageActions(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.log.info(f"************* test_valid_login *****************")
        self.lp.login("test@email.com", "abcabc")
        assert self.lpa.verify_avatar_image() == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.log.info(f"************* test_invalid_login *****************")
        result1 = self.lpa.verify_home_page_title()
        self.ts.mark(result1, "Title Verification Failed")

        self.lp.login("test@email.com", "abcabcas")
        result2 = self.lpa.verify_login_error_toast_message()
        self.ts.mark_final("test_invalid_login", result2, "login Uncussessful")


