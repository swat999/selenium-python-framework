from pageObjects.home.login_page_objects import LoginPageObjects
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPageActions(SeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.lpo = LoginPageObjects()

    def click_signup_button(self):

        self.click_element(self.lpo.signup_button)

    def click_login_link(self):

        self.click_element(self.lpo.login_link)

    def enter_email(self, email):

        self.enter_data_in_field(self.lpo.email_field, email)

    def enter_password(self, password):

        self.enter_data_in_field(self.lpo.password_field, password)

    def click_login_button(self):

        self.click_element(self.lpo.login_button)

    def verify_avatar_image(self):

        return self.is_element_present(self.lpo.avatar_image)

    def verify_login_error_toast_message(self):

        return self.is_element_present(self.lpo.login_error_toast)

    def get_page_title(self):
        return self.driver.title

    def verify_home_page_title(self):
        if 'login' in self.get_page_title():
            return True
        else:
            return False



