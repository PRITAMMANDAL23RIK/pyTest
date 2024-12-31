import time

import pytest
from selenium.webdriver.support.select import Select

from SelFramework.POM.HomePage import HomePage
from SelFramework.TestData.HomPage_test_data import HomePage_test_data
from SelFramework.utilities.BaseClass import BaseClass

class Test_two(BaseClass):
    def test_home(self,setup1,getData):
        log = self.setup_logging()
        log.info("Test Started")
        homepage = HomePage(self.driver)
        log.info(getData["firstname"])
        homepage.nameText().send_keys(getData["firstname"])
        homepage.emailText().send_keys(getData["email"])
        homepage.passwordText().send_keys("1234567")
        homepage.checkBoxClick().click()
        dropdown = Select(homepage.dropdownSelect())
        dropdown.select_by_visible_text(getData["gender"])
        homepage.submit().click()
        message = homepage.messageText().text
        log.info("message recived "+message)
        assert "Success" in message
        time.sleep(2)
        self.driver.refresh()


    @pytest.fixture(params=HomePage_test_data.test_Homepage_data)
    def getData(self,request):
        return request.param