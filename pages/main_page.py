import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config.urls import BASE_URL
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    URL = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(self.URL)
        self.wait_page_ready()

    @allure.step('Нажать кнопку «Войти в аккаунт»')
    def click_login_button(self):
        self.wait_page_ready()
        self.click(MainPageLocators.LOGIN_BUTTON)
