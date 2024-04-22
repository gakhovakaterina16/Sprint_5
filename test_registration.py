from selenium.webdriver.common.by import By

def test_successful_registration(driver, website_url):
    driver.get(website_url)

    button_personal_cabinet = driver.find_element(By.XPATH, "html/body/div/div/header/nav/a")
    button_personal_cabinet.click()
    registration_button = driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj")
    registration_button.click()

    name_input = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")
    email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    name_input.send_keys("gakhova_7")
    email_input.send_keys("gakhova_7@gmail.com")
    password_input.send_keys("12345678")

    registration_button_2 = driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")
    registration_button_2.click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


def test_registration_incorrect_password(driver, website_url):
    driver.get(website_url)

    button_personal_cabinet = driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    button_personal_cabinet.click()
    registration_button = driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj")
    registration_button.click()

    name_input = driver.find_element(By.XPATH, "//p[contains(text(),'Имя')]")
    email_input = driver.find_element(By.XPATH, "//p[contains(text(),'Email')]")
    password_input = driver.find_element(By.XPATH, "//p[contains(text(),'Пароль')]")

    name_input.send_keys("gakhova_7")
    email_input.send_keys("gakhova_7@gmail.com")
    password_input.send_keys("1234")

    registration_button_2 = driver.find_element(By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")
    registration_button_2.click()

    assert driver.find_element(By.CLASS_NAME, "input__error text_type_main-default").text() == "Некорректный пароль"
