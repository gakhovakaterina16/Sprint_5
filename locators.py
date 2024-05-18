from selenium.webdriver.common.by import By


class PersonalCabinetLocators:
    ENTER_BUTTON = (By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//html/body/div/div/header/nav/a")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")


class RegistrationLocators:
    BUTTON_PERSONAL_CABINET = (By.XPATH, "html/body/div/div/header/nav/a")
    REGISTRATION_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTRATION_BUTTON_2 = (By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")
    INCORRECT_PASSWORD_TEXT = (By.CLASS_NAME, "input__error text_type_main-default")


class TabsConstructorLocators:
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]/span[contains(text(), 'Булки')]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]/span[contains(text(), 'Соусы')]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG')]/span[contains(text(), 'Начинки')]")
