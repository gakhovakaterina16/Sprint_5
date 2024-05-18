from locators import PersonalCabinetLocators

URL = "https://stellarburgers.nomoreparties.site/"

class TestPersonalCabinetFunctionality:
    def test_enter_button(self, driver):
        driver.get(URL)

        button_enter = driver.find_element(*PersonalCabinetLocators.ENTER_BUTTON)
        button_enter.click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_personal_cabinet_button(self, driver, website_data):
        driver.get(URL)

        button_personal_cabinet = driver.find_element(*PersonalCabinetLocators.PERSONAL_CABINET_BUTTON)
        button_personal_cabinet.click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_authorization(self, driver, website_data):
        driver.get(URL])

        button_enter = driver.find_element(*PersonalCabinetLocators.ENTER_BUTTON)
        button_enter.click()

        email_input = driver.find_element(*PersonalCabinetLocators.EMAIL_INPUT)
        password_input = driver.find_element(*PersonalCabinetLocators.PASSWORD_INPUT)

        email_input.send_keys("gakhova_7@gmail.com")
        password_input.send_keys("12345678")

        button_enter_2 = driver.find_element(*PersonalCabinetLocators.LOGIN_BUTTON)
        button_enter_2.click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
