import logging
import os
import time

from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from traceback import print_stack
import utilities.custom_logger as cl


class SeleniumDriver:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        element = None
        loc_type = locator[0].lower()
        try:
            if loc_type == "id":
                element = self.driver.find_element(By.ID, locator[1])
            elif loc_type == "name":
                element = self.driver.find_element(By.NAME, locator[1])
            elif loc_type == "xpath":
                element = self.driver.find_element(By.XPATH, locator[1])
            elif loc_type == "css":
                element = self.driver.find_element(By.CSS_SELECTOR, locator[1])
            elif loc_type == "class":
                element = self.driver.find_element(By.CLASS_NAME, locator[1])
            elif loc_type == "linktext":
                element = self.driver.find_element(By.LINK_TEXT, locator[1])
            self.log.info(f"Found the element by locator type {locator[0]} and locator {locator[1]}")
        except:
            self.log.info(f"Cant find the element with given by type {locator[0]} and locator {locator[1]}")
            print_stack()
        return element

    def get_elements(self, locator):
        elements = []
        loc_type = locator[0].lower()
        try:
            if loc_type == "id":
                elements = self.driver.find_elements(By.ID, locator[1])
            elif loc_type == "name":
                elements = self.driver.find_elements(By.NAME, locator[1])
            elif loc_type == "xpath":
                elements = self.driver.find_elements(By.XPATH, locator[1])
            elif loc_type == "css":
                elements = self.driver.find_elements(By.CSS_SELECTOR, locator[1])
            elif loc_type == "class":
                elements = self.driver.find_elements(By.CLASS_NAME, locator[1])
            elif loc_type == "linktext":
                elements = self.driver.find_elements(By.LINK_TEXT, locator[1])
            self.log.info(f"Found the elements by locator type {locator[0]} and locator {locator[1]}")
        except:
            self.log.info(f"Cant find the element with given by type {locator[0]} and locator {locator[1]}")
            print_stack()
        return elements

    def click_element(self, locator):
        try:
            self.get_element(locator).click()
            self.log.info(f"clicked the element {locator[1]}")
        except:
            self.log.info(f"Unable to click the element {locator[1]}")
            print_stack()

    def enter_data_in_field(self, locator, data):
        try:
            self.get_element(locator).send_keys(data)
            self.log.info(f"filled the element {locator[1]} with {data} successfully")
        except:
            print_stack()
            self.log.info(f"Failed to enter data in {locator[1]}")

    def is_element_present(self, locator):
        try:
            element = self.get_element(locator)
            if element is not None:
                self.log.info(f"the element {element} is present")
                return True
            else:
                return False
        except:
            self.log.info(f"the element is not present {locator}")
            print_stack()
            return False

    def is_elements_present(self, locator):
        try:
            elements = self.get_elements(locator)
            if len(elements) > 1:
                self.log.info(f"The elements are present by locator {locator}")
                return True
            else:
                return False
        except:
            print_stack()
            self.log.info(f"The elements are not present by locator {locator}")
            return False

    def wait_for_element(self, locator, time_out, polling_time):
        try:
            element = None
            wait = WebDriverWait(self.driver, timeout=time_out, poll_frequency=polling_time,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            loc_type = locator[0].lower()

            if loc_type == "id":
                element = wait.until(ec.element_to_be_clickable(self.driver.find_element(By.ID, locator[1])))

            elif loc_type == "name":
                element = wait.until(ec.element_to_be_clickable(self.driver.find_element(By.NAME, locator[1])))

            elif loc_type == "xpath":
                element = wait.until(ec.element_to_be_clickable(self.driver.find_element(By.XPATH, locator[1])))

            elif loc_type == "css":
                element = wait.until(ec.element_to_be_clickable(self.driver.find_element(By.CSS_SELECTOR, locator[1])))

            elif loc_type == "class":
                element = wait.until(ec.element_to_be_clickable(self.driver.find_element(By.CLASS_NAME, locator[1])))

            elif loc_type == "linktext":
                element = wait.until(ec.element_to_be_clickable(self.driver.find_element(By.LINK_TEXT, locator[1])))

            self.log.info(f"waited for the element{locator} successfully")
            return element
        except:
            self.log.info(f"Unable to find the element with the by type {locator[0]} and locator {locator[1]}")
            print_stack()
            return None

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()
