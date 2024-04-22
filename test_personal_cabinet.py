from selenium.webdriver.common.by import By


def test_enter_button(driver, website_url):
    driver.get(website_url)

    button_enter = driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")
    button_enter.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_personal_cabinet_button(driver, website_url):
    driver.get(website_url)

    button_personal_cabinet = driver.find_element(By.XPATH, "html/body/div/div/header/nav/a")
    button_personal_cabinet.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_authorization(driver, website_url):
    driver.get(website_url)

    button_enter = driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")
    button_enter.click()

    email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    email_input.send_keys("gakhova_7@gmail.com")
    password_input.send_keys("12345678")

    button_enter_2 = driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")
    button_enter_2.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
