import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import configparser
import sys
from os.path import join



@pytest.fixture(scope='function')
def set_up(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://courses.letskodeit.com/")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()



