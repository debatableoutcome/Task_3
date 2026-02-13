import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_feed_locators import OrderFeedLocators
from config.urls import FEED_URL


class OrderFeedPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Открыть ленту заказов')
    def open_feed(self):
        self.driver.get(FEED_URL)
        self.wait.until(lambda d: '/feed' in d.current_url)
        self.wait.until(EC.presence_of_element_located(OrderFeedLocators.ORDER_CARD))

    @allure.step('Кликнуть по первому заказу')
    def click_first_order(self):
        self.driver.find_element(*OrderFeedLocators.ORDER_CARD).click()

    @allure.step('Дождаться открытия модального окна заказа')
    def wait_order_modal_opened(self):
        self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL_OPENED))

    @allure.step('Проверить, что модальное окно открыто')
    def is_modal_opened(self):
        return self.wait.until(
            EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL)
        )

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.driver.find_element(*OrderFeedLocators.MODAL_CLOSE).click()

    @allure.step('Получить общий счетчик заказов')
    def get_total_counter(self):
        return self.driver.find_element(*OrderFeedLocators.TOTAL_COUNTER).text

    @allure.step('Получить счетчик заказов за сегодня')
    def get_today_counter(self):
        return self.driver.find_element(*OrderFeedLocators.TODAY_COUNTER).text

    @allure.step('Получить номера заказов в работе')
    def get_in_progress_numbers(self):
        items = self.driver.find_elements(*OrderFeedLocators.IN_PROGRESS_LIST)
        return [i.text for i in items]
