from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_feed_locators import OrderFeedLocators
from config.urls import FEED_URL

class OrderFeedPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_feed(self):
        self.driver.get(FEED_URL)
        self.wait.until(lambda d: '/feed' in d.current_url)
        self.wait.until(EC.presence_of_element_located(OrderFeedLocators.ORDER_CARD))

    def click_first_order(self):
        self.driver.find_element(*OrderFeedLocators.ORDER_CARD).click()

    def wait_order_modal_opened(self):
        self.wait.until(EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL_OPENED))
        
    def is_modal_opened(self):
        return self.wait.until(
            EC.visibility_of_element_located(OrderFeedLocators.ORDER_MODAL)
        )

    def close_modal(self):
        self.driver.find_element(*OrderFeedLocators.MODAL_CLOSE).click()

    def get_total_counter(self):
        return self.driver.find_element(*OrderFeedLocators.TOTAL_COUNTER).text

    def get_today_counter(self):
        return self.driver.find_element(*OrderFeedLocators.TODAY_COUNTER).text

    def get_in_progress_numbers(self):
        items = self.driver.find_elements(*OrderFeedLocators.IN_PROGRESS_LIST)
        return [i.text for i in items]
