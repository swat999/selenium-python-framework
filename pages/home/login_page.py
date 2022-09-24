
from pageActions.home.login_page_actions import LoginPageActions
import logging
import utilities.custom_logger as cl


class LoginPage:

    log = cl.custom_logger(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        lpa = LoginPageActions(self.driver)
        lpa.click_signup_button()
        lpa.click_login_link()
        lpa.enter_email(email)
        lpa.enter_password(password)
        lpa.click_login_button()


