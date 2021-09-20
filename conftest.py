from config import TestData
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


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
            # web_driver = webdriver.Chrome(chrome_driver)
            caps = {'browserName': os.getenv('BROWSER', 'chrome')}
            web_driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def info_logging(request):
    request.cls.plogger = logging.getLogger("apiTest")
    request.cls.plogger.setLevel( logging.INFO ) 

# def setUp(self):
#     caps = {'browserName': os.getenv('BROWSER', 'chrome')}
#     self.browser = webdriver.Remote(
#         command_executor='http://localhost:4444/wd/hub',
#         desired_capabilities=caps
#     )