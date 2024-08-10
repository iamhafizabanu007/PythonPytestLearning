import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
import time
from Utilities.readproperties import ReadConfig
from Utilities.customelogger import LogGen
from Utilities import XLUtil

class Test_002_DDT_Login:
    # base_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username="admin@yourstore.com"
    # password="admin"
    r=ReadConfig()
    base_url=r.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    # username=r.getUserEmail()
    # password=r.getUserPassword()
    logger=LogGen.loggen()

    # def test_homepagetitle(self, setip):
    #     self.logger.info("************************ Test _001__Login")
    #     self.driver.save_screenshot(".\\Screenshott\\" + "login.png")
    #     self.driver=setip
    #     self.logger.info("************************ Test _001__Login __pass")
    #     self.driver.get(self.base_url)
    #     title=self.driver.title
        #
        # if title=="your store. Login":
        #     assert True
        #     # self.logger.info("************************ Test _001__Login __pass")
        # else:
        #     self.driver.save_screenshot(".\\Screenshot\\"+"login.png")
        #     assert False
        # self.driver.close()
    @pytest.mark.regression
    def test_login_ddt(self, setip):
        time.sleep(4)
        self.driver=setip
        self.driver.get(self.base_url)
        time.sleep(4)
        self.lp=Login(self.driver)
        time.sleep(4)
        sheetName = "Sheet1"
        self.rows=XLUtil.getRowCount(self.path,sheetName)
        print("rows : " , self.rows)
        ls_emptu=[]
        for r in range(2, self.rows + 1):
            self.user=XLUtil.readData(self.path, sheetName, r,1)
            self.password = XLUtil.readData(self.path, sheetName, r, 2)
            self.exp = XLUtil.readData(self.path, sheetName, r, 3)
            self.lp.username(self.user)
            self.lp.password(self.password)
            self.lp.login()
            time.sleep(5)
            ac_title=self.driver.title
            ex_title="somethig"

            if ac_title==ex_title:
                if self.exp=="Pass":
                    self.logger.info("**** passs")
                    self.lp.logout()
                    ls_emptu.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("**** fail")
                    self.lp.logout()
                    ls_emptu.append("Fail")
            elif ac_title!=ex_title:
                if self.exp=="Pass":
                    self.logger.info("**** fail")
                    self.lp.logout()
                    ls_emptu.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("**** pass")
                    self.lp.logout()
                    ls_emptu.append("Pass")
        if "Fail" not in ls_emptu:
            self.logger.info("Login is pass")
            self.driver.close()
            assert  True
        else:
            self.logger.info("Login is faile")
            self.driver.close()
            assert  False