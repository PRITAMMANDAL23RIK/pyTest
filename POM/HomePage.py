from selenium.webdriver.common.by import By

from SelFramework.POM.CheckoutPage import CheckoutPage


class HomePage:
    def __init__(self, driver):
        self.driver=driver

    shop = (By.LINK_TEXT, "Shop")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    expCheck = (By.ID, "exampleCheck1")
    name = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    drpdown = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.CSS_SELECTOR, "input[type='submit']")
    alertMessage = (By.CLASS_NAME, "alert")

    def shopPge(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def nameText(self):
        return self.driver.find_element(*HomePage.name)

    def emailText(self):
        return self.driver.find_element(*HomePage.email)

    def passwordText(self):
        return self.driver.find_element(*HomePage.password)

    def checkBoxClick(self):
        return self.driver.find_element(*HomePage.expCheck)

    def dropdownSelect(self):
        return self.driver.find_element(*HomePage.drpdown)

    def submit(self):
        return self.driver.find_element(*HomePage.submitBtn)

    def messageText(self):
        return self.driver.find_element(*HomePage.alertMessage)



