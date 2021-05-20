from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkBox = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
    country = (By.XPATH, "//input[@id = 'country']")
    countryName = (By.LINK_TEXT, "India")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CSS_SELECTOR, "div[class*='success']")

    def clickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.message)

