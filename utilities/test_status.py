from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging


class TestStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.resultList = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.log.info(f"### VERIFICATION SUCCESSFUL ### :: {result_message}")
                    self.resultList.append(True)
                else:
                    self.log.info(f"### VERIFICATION UNSUCCESSFUL ### :: {result_message}")
                    self.resultList.append(False)
                    self.screenShot(result_message)
            else:
                self.log.info(f"### VERIFICATION UNSUCCESSFUL ### :: {result_message}")
                self.resultList.append(False)
                self.screenShot(result_message)

        except:
            self.resultList.append(False)
            self.log.error(f" ### ERROR OCCURRED ### :: {result_message}")
            self.screenShot(result_message)

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        self.set_result(result, result_message)

        if False in self.resultList:
            self.log.error(f"{test_name} :: ### TEST FAILED ###")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(f" {test_name} : ### TEST SUCCESSFUL ###")
            self.resultList.clear()
            assert True == True





