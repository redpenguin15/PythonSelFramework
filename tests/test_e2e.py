
from PycharmProjects.PythonSelFramework.pageObjects.CheckOutPage import CheckOutPage
from PycharmProjects.PythonSelFramework.pageObjects.ConfirmPage import ConfirmPage
from PycharmProjects.PythonSelFramework.pageObjects.HomePage import HomePage
from PycharmProjects.PythonSelFramework.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        log.info("Getting all card titles.")
        cards = checkOutPage.getCardTitles()
        confirmPage = ConfirmPage(self.driver)

        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            log.info(cardText)
            if cardText == 'Blackberry':
                checkOutPage.getCardFooter()[i].click()
        #
        checkOutPage.checkOutButton().click()
        # assert "Blackberry" == (self.driver.find_element_by_css_selector("h4[class='media-heading']").text)
        #
        checkOutPage.finalCheckout().click()
        #
        log.info("Entering country name Ind")

        confirmPage.getLocation().send_keys("ind")

        self.verifyLinkPresence("India")
        confirmPage.selectCountry().click()
        confirmPage.clickCheckBox().click()
        confirmPage.purchaseButton().click()
        message = confirmPage.successMessage().text
        log.info("Text received from application is" + message)

        assert "Success! Thank you!" in message

