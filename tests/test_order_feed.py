import allure
from pages.order_feed_page import OrderFeedPage


@allure.suite('Лента заказов')
class TestOrderFeed:

    @allure.title('Клик по заказу открывает модальное окно')
    def test_order_modal_opens(self, driver):
        page = OrderFeedPage(driver)

        page.open_feed()
        page.click_first_order()
        page.wait_order_modal_opened()
