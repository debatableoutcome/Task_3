from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.urls import FORGOT_PASSWORD_URL
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    def open_page(self):
        self.open(FORGOT_PASSWORD_URL)
        self.wait.until(EC.url_contains('/forgot-password'))

    def enter_email(self, email):
        self.fill(ForgotPasswordLocators.EMAIL_INPUT, email)

    def click_restore(self):
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)
        self.wait.until(EC.url_contains('/reset-password'))
