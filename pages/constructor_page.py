import allure

from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators


class ConstructorPage(BasePage):

    def _get_counter_from_card(self, card):
        counters = card.find_elements(*ConstructorLocators.INGREDIENT_COUNTER)
        if not counters:
            return 0
        text = counters[0].text.strip()
        return int(text) if text.isdigit() else 0

    @allure.step('Нажать «Конструктор»')
    def click_constructor_header(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.is_visible(ConstructorLocators.INGREDIENTS_LIST)

    @allure.step('Открыть «Лента заказов»')
    def click_order_feed_header(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_url_contains('/feed')
        self.wait_present(OrderFeedLocators.ORDER_CARD)

    @allure.step('Проверить, что открыт конструктор')
    def is_constructor_opened(self):
        self.is_visible(ConstructorLocators.INGREDIENTS_LIST)
        return '/feed' not in self.get_current_url()

    @allure.step('Проверить, что открыта лента заказов')
    def is_order_feed_opened(self):
        return '/feed' in self.get_current_url() and self.is_visible(OrderFeedLocators.ORDER_CARD) is not None

    @allure.step('Кликнуть по ингредиенту')
    def click_first_ingredient(self):
        self.is_visible(ConstructorLocators.INGREDIENTS_LIST)
        self.click(ConstructorLocators.INGREDIENT_CARD)

    @allure.step('Дождаться модалки деталей ингредиента')
    def wait_ingredient_modal_opened(self):
        self.is_visible(ConstructorLocators.INGREDIENT_MODAL)
        self.is_visible(ConstructorLocators.INGREDIENT_MODAL_STATS)

    @allure.step('Проверить, что модалка ингредиента открыта')
    def is_ingredient_modal_opened(self):
        return self.is_visible(ConstructorLocators.INGREDIENT_MODAL) is not None

    @allure.step('Закрыть модалку по крестику')
    def close_modal(self):
        self.click(ConstructorLocators.MODAL_CLOSE_BUTTON)
        self.wait_not_visible(ConstructorLocators.INGREDIENT_MODAL)

    @allure.step('Проверить, что модалка ингредиента закрыта')
    def is_ingredient_modal_closed(self):
        return self.wait_not_visible(ConstructorLocators.INGREDIENT_MODAL)

    @allure.step('Получить каунтер первого ингредиента')
    def get_first_ingredient_counter(self):
        card = self.wait_present(ConstructorLocators.INGREDIENT_CARD)
        return self._get_counter_from_card(card)

    @allure.step('Добавить первый ингредиент в конструктор drag&drop')
    def add_first_ingredient_to_constructor(self):
        self.drag_and_drop_on_element(
            ConstructorLocators.INGREDIENT_CARD,
            ConstructorLocators.CONSTRUCTOR_DROPZONE
        )

    @allure.step('Добавить булку в конструктор')
    def add_bun_to_constructor(self):
    
        self.drag_and_drop_on_element(
            ConstructorLocators.FIRST_BUN_CARD,
            ConstructorLocators.CONSTRUCTOR_DROPZONE
        )

    @allure.step('Добавить соус в конструктор')
    def add_sauce_to_constructor(self):
        self.drag_and_drop_on_element(
            ConstructorLocators.FIRST_SAUCE_CARD,
            ConstructorLocators.CONSTRUCTOR_DROPZONE
        )

    @allure.step('Получить каунтер булки')
    def get_bun_counter(self):
        bun_card = self.wait_present(ConstructorLocators.FIRST_BUN_CARD)
        return self._get_counter_from_card(bun_card)

    @allure.step('Получить каунтер первого соуса')
    def get_sauce_counter(self):
        sauce_card = self.wait_present(ConstructorLocators.FIRST_SAUCE_CARD)
        return self._get_counter_from_card(sauce_card)

    @allure.step('Оформить заказ')
    def click_order(self):
        self.click(ConstructorLocators.ORDER_BUTTON)

    @allure.step('Дождаться окна успешного заказа')
    def wait_order_success(self):
        self.is_visible(ConstructorLocators.ORDER_SUCCESS_TEXT)

    @allure.step('Проверить, что заказ успешно создан')
    def is_order_success_visible(self):
        return self.is_visible(ConstructorLocators.ORDER_SUCCESS_TEXT) is not None
