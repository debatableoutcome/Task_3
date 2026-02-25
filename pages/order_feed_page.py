import allure

from pages.base_page import BasePage
from config.urls import FEED_URL
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    @allure.step('Открыть ленту заказов')
    def open_feed(self):
        self.open(FEED_URL)
        self.wait_url_contains('/feed')
        self.wait_present(OrderFeedLocators.ORDER_CARD)

    @allure.step('Кликнуть по первому заказу')
    def click_first_order(self):
        self.click(OrderFeedLocators.ORDER_CARD)

    @allure.step('Дождаться открытия модального окна заказа')
    def wait_order_modal_opened(self):
        self.is_visible(OrderFeedLocators.ORDER_MODAL_OPENED)

    @allure.step('Проверить, что модальное окно открыто')
    def is_modal_opened(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL_OPENED) is not None

    @allure.step('Проверить, что открыта лента заказов')
    def is_feed_opened(self):
        return self.current_url_contains('/feed') and self.is_visible(OrderFeedLocators.ORDER_CARD) is not None

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click(OrderFeedLocators.MODAL_CLOSE_BUTTON)
        self.wait_not_visible(OrderFeedLocators.ORDER_MODAL_OPENED)
