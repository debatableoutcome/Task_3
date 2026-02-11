from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.urls import BASE_URL
from locators.main_page_locators import MainPageLocators


class MainPage:

    URL = BASE_URL

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def click_login_button(self):
        button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        button.click()
