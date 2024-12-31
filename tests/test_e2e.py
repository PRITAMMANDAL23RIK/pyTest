import time


from SelFramework.POM.HomePage import HomePage
from SelFramework.utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class Test_one(BaseClass):
    def test_e2e(self,setup1):
        choseProduct = "Blackberry"
        log = self.setup_logging()
        log.info("Test started")
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopPge()
        productList = checkoutpage.prodList()
        log.info("Now recive all the product list")
        for product in productList:
            prod = checkoutpage.prodPc(product)
            log.info(prod.text)
            if prod.text == choseProduct:
                checkoutpage.correctPd(product).click()
                break
        else:
            log.error("product not found")
        checkoutpage.checkBut().click()
        confirmpage = checkoutpage.succBut()
        log.info("entering country name as ind")
        confirmpage.countryConf().send_keys("ind")
        self.waiting((confirmpage.suggestionBox))
        countries = confirmpage.suggestedCountries()
        for country in countries:
            if country.text == "India":
                country.click()
                break
        confirmpage.clickCheckBox().click()
        confirmpage.purchaseBtn().click()
        successText = confirmpage.successMessage().text
        log.info("text message recieved "+successText)
        assert "Success! Thank you!" in successText

        time.sleep(2)

