import allure

from pages.base_page import BasePage
from config.urls import BASE_URL
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    URL = BASE_URL

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    @allure.step('Открыть главную страницу')
    def open(self):
        super().open(self.URL)
        self.wait_page_ready()

    @allure.step('Нажать кнопку «Войти в аккаунт»')
    def click_login_button(self):
        self.wait_page_ready()
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Нажать «Лента заказов»')
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Нажать «Конструктор»')
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

