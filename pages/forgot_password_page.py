import allure

from pages.base_page import BasePage
from config.urls import FORGOT_PASSWORD_URL
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def open_page(self):
        self.open(FORGOT_PASSWORD_URL)
        self.wait_url_contains('/forgot-password')

    @allure.step('Ввести email для восстановления')
    def enter_email(self, email):
        self.fill(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step('Нажать кнопку "Восстановить"')
    def click_restore(self):
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)
        self.wait_url_contains('/reset-password')
