import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
@pytest.fixture(scope="function")
def website_url():
    return "https://stellarburgers.nomoreparties.site/"
