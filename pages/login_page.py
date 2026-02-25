import allure

from pages.base_page import BasePage
from config.urls import LOGIN_URL
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    URL = LOGIN_URL

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    @allure.step('Нажать «Восстановить пароль»')
    def click_forgot_password(self):
        self.wait_page_ready()
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Авторизоваться')
    def login(self, email, password):
        self.wait_page_ready()
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Дождаться открытия страницы логина')
    def wait_login_page_opened(self):
        self.wait_page_ready()
        self.wait_url_contains('/login')
