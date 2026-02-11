from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.urls import LOGIN_URL
from locators.login_page_locators import LoginPageLocators


class LoginPage:

    URL = LOGIN_URL

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_forgot_password(self):
        link = self.wait.until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK))
        link.click()
