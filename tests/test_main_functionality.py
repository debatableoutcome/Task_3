import allure

from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions as EC

class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        constructor_page.click_constructor_header(MainPageLocators.CONSTRUCTOR_BUTTON)

        assert '/' in driver.current_url

    @allure.title('Переход по клику на «Лента заказов»')
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        constructor_page.click_order_feed_header(MainPageLocators.ORDER_FEED_BUTTON)


    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_ingredient_details_modal_opens(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        constructor_page.click_first_ingredient()
        constructor_page.wait_ingredient_modal_opened()

    @allure.title('Окно деталей ингредиента закрывается по крестику')
    def test_ingredient_details_modal_closes(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        constructor_page.click_first_ingredient()
        constructor_page.wait_ingredient_modal_opened()
        constructor_page.close_modal()

    @allure.title('При добавлении ингредиента увеличивается каунтер')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()

        before = constructor_page.get_sauce_counter()
        constructor_page.add_sauce_to_constructor()
        after = constructor_page.get_sauce_counter()

        assert after == before + 1

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, driver, authorized_user):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        constructor_page.add_first_ingredient_to_constructor()
        constructor_page.click_order()
        constructor_page.wait_order_success()

    @allure.title('Каунтер булки увеличивается до 2')
    def test_bun_counter_is_two(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        assert constructor_page.get_bun_counter() == 0

        constructor_page.add_bun_to_constructor()

        assert constructor_page.get_bun_counter() == 2


    @allure.title('Каунтер ингредиента (не булка) увеличивается до 1')
    def test_non_bun_counter_is_one(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        assert constructor_page.get_sauce_counter() == 0

        constructor_page.add_sauce_to_constructor()

        assert constructor_page.get_sauce_counter() == 1


    @allure.title('Каунтер ингредиента (не булка) после двух добавлений равен 2')
    def test_non_bun_counter_is_two_after_double_add(self, driver):
        main_page = MainPage(driver)
        constructor_page = ConstructorPage(driver)

        main_page.open()
        assert constructor_page.get_sauce_counter() == 0

        constructor_page.add_sauce_to_constructor()
        constructor_page.add_sauce_to_constructor()

        assert constructor_page.get_sauce_counter() == 2
