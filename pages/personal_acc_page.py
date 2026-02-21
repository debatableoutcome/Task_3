import allure

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import locators.personal_acc_locators as personal_locators
from locators.main_page_locators import MainPageLocators


class PersonalAccPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    @allure.step('Нажать «Личный кабинет»')
    def click_personal_account(self):
        self.wait_page_ready()
        self.click(personal_locators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Открыть профиль авторизованного пользователя')
    def open_profile_as_authorized_user(self, email, password):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)

        main_page.open()
        self.click_personal_account()
        login_page.login(email, password)
        self.click_personal_account()
        self.wait_profile_opened()

    @allure.step('Кликнуть «Выход»')
    def click_logout(self):
        self.wait_page_ready()
        self.wait_url_contains('/account')
        self.click(personal_locators.LOGOUT_BUTTON)

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click_logout()
        self.wait_url_contains('/login')
        self.is_visible(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Дождаться открытия профиля')
    def wait_profile_opened(self):
        self.wait_page_ready()
        self.wait_url_contains('/account/profile')

    @allure.step('Перейти в «История заказов»')
    def click_order_history(self):
        self.wait_page_ready()
        self.click(personal_locators.ORDER_HISTORY_MENU_LINK)

    @allure.step('Дождаться открытия истории заказов')
    def wait_order_history_opened(self):
        self.wait_page_ready()
        self.wait_url_contains('/account/order-history')



    @allure.step('Дождаться редиректа на логин')
    def wait_login_opened(self):
        self.wait_page_ready()
        self.wait_url_contains('/login')
