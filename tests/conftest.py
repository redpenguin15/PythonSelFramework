import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name =='chrome':
        driver = webdriver.Chrome(executable_path=r"C:\Users\anupa\Desktop\testing\chromedriver.exe")
    elif browser_name =='firefox':
        driver = webdriver.Firefox(executable_path = r"C:\Users\anupa\Desktop\testing\geckodriver.exe")
    elif browser_name =='internet_explorer':
        #IE driver
        print("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
