from config import TestData
import openpyxl
from bcra_page import BCRApage
from test_base import BaseTest
import pytest
import schedule
import time

@pytest.mark.usefixtures('info_logging')
class Test_Script(BaseTest):

    def test_script(self):
        self.BCRApage = BCRApage(self.driver)
        self.BCRApage.SendDateDesde()
        self.BCRApage.SendDateHasta()
        self.export_values()
    

    def export_values(self):
        Dat = self.BCRApage.get_table_data()
        wb = openpyxl.Workbook()
        ws = wb.active
        for data in zip(Dat):
            ws.append(data)
        wb.save(filename=f"{TestData.Serie}-{TestData.FechaDesde}-{TestData.FechaHasta}.xlsx")
    
    # schedule.every().monday.do(test_date)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


# def main():
#     foo = Test_Data()
#     foo.test_date()

# if __name__ == "__main__":
#     main()


#pepe
#pepito
        
    



    

    


            
            