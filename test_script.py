from config import TestData
import openpyxl
from bcra_page import BCRApage
from test_base import BaseTest
import pytest
import schedule
import time

# pepe
# correr: pytest test_script.py::Test_Script::test_generate_excel

@pytest.mark.usefixtures('info_logging')
class Test_Script(BaseTest):

    def test_generate_excel(self):

        self.BCRApage = BCRApage(self.driver)
        self.BCRApage.SendDateDesde()
        self.BCRApage.SendDateHasta()
        self.export_values()
    

    def export_values(self):
        
        Dat = self.BCRApage.get_table_data()
        if Dat is True:
            wb = openpyxl.Workbook()
            ws = wb.active
            for data in zip(Dat):
                ws.append(data)
            wb.save(filename=f"{TestData.Serie}-{TestData.FechaDesde}-{TestData.FechaHasta}.xlsx")
        else:
            raise Exception("No se pudo extraer los valores. Ingresar la fecha nuevamente")
        
    # schedule.every().monday.do(test_date)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

        
    



    

    


            
            