from locators import RegistrationLocators
from faker import Faker


fake = Faker()


class TestRegistration:
    def test_successful_registration(self, driver, website_data):
        driver.get(website_data["url"])

        button_personal_cabinet = driver.find_element(*RegistrationLocators.BUTTON_PERSONAL_CABINET)
        button_personal_cabinet.click()
        registration_button = driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON)
        registration_button.click()

        name_input = driver.find_element(*RegistrationLocators.NAME_INPUT)
        email_input = driver.find_element(*RegistrationLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)

        name_input.send_keys("gakhova_7")
        email_input.send_keys(fake.email())
        password_input.send_keys("12345678")

        registration_button_2 = driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON_2)
        registration_button_2.click()

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_registration_incorrect_password(self, driver, website_data):
        driver.get(website_data["url"])

        button_personal_cabinet = driver.find_element(*RegistrationLocators.BUTTON_PERSONAL_CABINET)
        button_personal_cabinet.click()
        registration_button = driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON)
        registration_button.click()

        name_input = driver.find_element(*RegistrationLocators.NAME_INPUT)
        email_input = driver.find_element(*RegistrationLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegistrationLocators.PASSWORD_INPUT)

        name_input.send_keys("gakhova_7")
        email_input.send_keys("gakhova_7@gmail.com")
        password_input.send_keys("1234")

        registration_button_2 = driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON_2)
        registration_button_2.click()

        assert driver.find_element(*RegistrationLocators.INCORRECT_PASSWORD_TEXT).text() == "Некорректный пароль"
