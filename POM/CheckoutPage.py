from selenium.webdriver.common.by import By

from SelFramework.POM.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver=driver

    products = (By.XPATH, "//app-card/div")
    prod = (By.XPATH, "div/h4/a")
    crrPd = (By.XPATH, "div[2]/button")
    checkBt = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    btnSucc = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def prodList(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def prodPc(self,product):
        return product.find_element(*CheckoutPage.prod)

    def correctPd(self,product):
        return product.find_element(*CheckoutPage.crrPd)

    def checkBut(self):
        return self.driver.find_element(*CheckoutPage.checkBt)

    def succBut(self):
        self.driver.find_element(*CheckoutPage.btnSucc).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
