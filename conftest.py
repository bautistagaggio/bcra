import pytest
from selenium import webdriver
import logging

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path='chromedriver.exe')
    request.cls.driver = web_driver
    yield
    # web_driver.close()

@pytest.fixture(scope="class")
def info_logging(request):
    request.cls.plogger = logging.getLogger("apiTest")
    request.cls.plogger.setLevel( logging.INFO ) 