from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from Utilities import configReader

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def click(self,locator):
        if str(locator).endswith(("_XPATH")):
            self.driver.find_element_by_xpath(configReader.readConfig("locators",locator)).click()
        elif str(locator).endswith(("_CSS")):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators",locator)).click()

    def type(self,locator,value):
        if str(locator).endswith(("_XPATH")):
            self.driver.find_element_by_xpath(configReader.readConfig("locators",locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators",locator)).send_keys(value)

    def select(self,locator,value):
        global dropdown
        if str(locator).endswith(("_XPATH")):
            dropdown=self.driver.find_element_by_xpath(configReader.readConfig("locators",locator))
        elif str(locator).endswith(("_CSS")):
            dropdown=self.driver.find_element_by_css_selector(configReader.readConfig("locators",locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)