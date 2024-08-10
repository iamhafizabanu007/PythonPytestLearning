import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
import time
from Utilities.readproperties import ReadConfig
from Utilities.customelogger import LogGen

class Test_001_Login:
    # base_url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username="admin@yourstore.com"
    # password="admin"
    r=ReadConfig()
    base_url=r.getApplicationURL()
    username=r.getUserEmail()
    password=r.getUserPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homepagetitle(self, setip):
        self.logger.info("************************ Test _001__Login")
        self.driver.save_screenshot(".\\Screenshott\\" + "login.png")
        self.driver=setip
        self.logger.info("************************ Test _001__Login __pass")
        self.driver.get(self.base_url)
        title=self.driver.title
        #
        # if title=="your store. Login":
        #     assert True
        #     # self.logger.info("************************ Test _001__Login __pass")
        # else:
        #     self.driver.save_screenshot(".\\Screenshot\\"+"login.png")
        #     assert False
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setip):
        time.sleep(4)
        self.driver=setip
        self.driver.get(self.base_url)
        time.sleep(4)
        self.lp=Login(self.driver)
        time.sleep(4)
        self.lp.username(self.username)
        time.sleep(4)
        self.lp.password(self.password)
        time.sleep(4)
        self.lp.login()
        time.sleep(4)
        title = self.driver.title
        if title!="your store. login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshott\\" + "login.png")
            assert False
            self.logger.error("************************ Test _001__Login __pass")
        self.driver.close()