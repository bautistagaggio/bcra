import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By



"""
/**
 ?                          THIS CLASS REPRESENTS THE PARENT CLASS FOR ALL WEB PAGES
*/"""

### it contains all the generic methods and utilities for ALL pages ###

class BasePage: 

    ############################# CONSTRUCTOR ###################################

    def __init__(self, driver):
        self.driver = driver

    ############################## ACTIONS #####################################
    
    def Wait_for_Existence(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))

    def get_object(self, by_locator):
        object = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return object

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator)).click()
    
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def get_elements_text(self, by_locator):
        texts = []
        matched_elements = self.driver.find_elements_by_xpath(by_locator)
        for matched_element in matched_elements:
            if not matched_element:
                continue 
            text = matched_element.text
            texts.append(text)
        return texts
    
    