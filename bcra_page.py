
from test_base import BaseTest
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage
from config import TestData
import time




"""
/**
 ?  -----------------------THIS CLASS CONTAINS ALL THE OBJECTS AND THEIR INTERACTIONS WITHIN HOME PAGE --------------------------------------------------        
*/"""


class BCRApage(BasePage):

    ###############################################   OBJECT SELECTORS   #########################################

    FechaDesde = (By.XPATH, "(//input[@name='fecha_desde'])[1]")
    FechaHasta = (By.XPATH, "(//input[@name='fecha_hasta'])[1]")
    Consultar = (By.XPATH, "//button[@class='btn btn-primary btn-sm']")
    Tabla = ("//tbody")
    

    ###############################################   OBJECT SELECTORS   #########################################

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Series[TestData.Serie])
        self.driver.maximize_window()
    
    def SendDateDesde(self):
        time.sleep(1)
        self.do_send_keys(self.FechaDesde,TestData.FechaDesde[0])
        self.do_send_keys(self.FechaDesde,TestData.FechaDesde[1])
        self.do_send_keys(self.FechaDesde,TestData.FechaDesde[2])

    def SendDateHasta(self):
        time.sleep(1)
        self.do_send_keys(self.FechaHasta,TestData.FechaHasta[0])
        self.do_send_keys(self.FechaHasta,TestData.FechaHasta[1])
        self.do_send_keys(self.FechaHasta,TestData.FechaHasta[2])
        self.do_click(self.Consultar)
    
    def get_table_data(self):
        time.sleep(1)
        return self.get_elements_text(self.Tabla)
    



    