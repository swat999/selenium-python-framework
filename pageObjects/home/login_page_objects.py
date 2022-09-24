from selenium.webdriver.common.by import By

class LoginPageObjects():
    '''
        locator types = id, name, xpath, css, class, linktext
    '''
    #  locators
    signup_button = ["linktext", "Sign up now"]
    login_link = ["linktext", "Login"]
    email_field = ["Id", "email"]
    password_field = ["ID", "password"]
    login_button = ["Xpath", "//*[@type='submit']"]
    avatar_image = ["class", "zl-navbar-rhs-img"]
    login_error_toast = ["Xpath", "//*[@class='form-group has-error']/span"]
