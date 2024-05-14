import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def website_data():
    url = "https://stellarburgers.nomoreparties.site/"
    return {"url": url}
