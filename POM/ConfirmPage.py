from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver=driver

    country = (By.ID, "country")
    suggestionBox = (By.CLASS_NAME, "suggestions")
    allCountry = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    checkBox = (By.XPATH, "//label[@for='checkbox2']")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    sucess = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def countryConf(self):
        return self.driver.find_element(*ConfirmPage.country)

    def suggestedCountries(self):
        return self.driver.find_elements(*ConfirmPage.allCountry)

    def clickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def purchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.sucess)