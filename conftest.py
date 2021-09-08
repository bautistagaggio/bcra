from config import TestData
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        chrome_driver = ChromeDriverManager().install()
        if TestData.Headless == "On":   
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            web_driver = webdriver.Chrome(chrome_driver, options=options)
        else:
            web_driver = webdriver.Chrome(chrome_driver)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def info_logging(request):
    request.cls.plogger = logging.getLogger("apiTest")
    request.cls.plogger.setLevel( logging.INFO ) 