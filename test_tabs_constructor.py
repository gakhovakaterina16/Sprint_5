from locators import TabsConstructorLocators


class TestConstructorTabs:
    def test_buns_tab_click(self, website_data):
        driver.get(website_data["url"])

        buns_tab = driver.get(*TabsConstructorLocators.BUNS_TAB)
        sauces_tab = driver.get(*TabsConstructorLocators.SAUCES_TAB)

        sauces_tab.click()
        buns_tab.click()

        assert driver.find_element(*TabsConstructorLocators).text() == "Булки"

    def test_sauces_tab_click(self, website_data):
        driver.get(website_data["url"])

        sauces_tab = driver.get(*TabsConstructorLocators.SAUCES_TAB)

        sauces_tab.click()

        assert driver.find_element(*TabsConstructorLocators).text() == "Соусы"

    def test_fillings_tab_click(self, website_data):
        driver.get(website_data["url"])

        fillings_tab = driver.get(*TabsConstructorLocators.SAUCES_TAB)

        fillings_tab.click()

        assert driver.find_element(*TabsConstructorLocators).text() == "Начинки"
