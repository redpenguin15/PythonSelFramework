from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # cardFooter = (By.XPATH, "div/h4/a")
    cardFooter = (By.CSS_SELECTOR,".card-footer button")
    checkOut_1 = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    checkOut_2 = (By.XPATH, "//button[@class = 'btn btn-success']")

    #
    # checkOut = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    # checkout1 = (By.XPATH,"//button[@class='btn btn-success']")
    # #a[class*='btn-primary']"

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOut_1)

    def finalCheckout(self):
        return self.driver.find_element(*CheckOutPage.checkOut_2)

