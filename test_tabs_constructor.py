from locators import TabsConstructorLocators

URL = "https://stellarburgers.nomoreparties.site/"

class TestConstructorTabs:
    def test_buns_tab_click(self, driver):
        driver.get(URL)

        buns_tab = driver.find_element(*TabsConstructorLocators.BUNS_TAB)
        sauces_tab = driver.find_element(*TabsConstructorLocators.SAUCES_TAB)

        sauces_tab.click()
        buns_tab.click()

        assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")

    def test_sauces_tab_click(self, driver):
        driver.get(URL)

        sauces_tab = driver.find_element(*TabsConstructorLocators.SAUCES_TAB)

        sauces_tab.click()

        assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")

    def test_fillings_tab_click(self, driver):
        driver.get(URL)

        fillings_tab = driver.find_element(*TabsConstructorLocators.FILLINGS_TAB)

        fillings_tab.click()

        assert "tab_tab_type_current__2BEPc" in fillings_tab.get_attribute("class")