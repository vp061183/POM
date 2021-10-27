import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities import configReader
import time

@pytest.fixture(params=["chrome"],scope="function")
def get_browser(request):
    global driver
    if request.param =="chrome":
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    driver.get(configReader.readConfig("basic info","testiturl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    time.sleep(20)
    driver.quit()