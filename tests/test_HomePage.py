import pytest

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select

from PycharmProjects.PythonSelFramework.TestData.HomePageData import HomePageData
from PycharmProjects.PythonSelFramework.pageObjects.HomePage import HomePage
from PycharmProjects.PythonSelFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["first_name"])
        homepage.getEmail().send_keys(getData["last_name"])
        homepage.getCheckbox().click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()
        alert_text = homepage.getSuccessMessage().text
        assert "Success" in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase3"))
    def getData(self, request):
        return request.param
