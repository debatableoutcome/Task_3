import allure

from pages.base_page import BasePage
import locators.personal_acc_locators as personal_locators


class PersonalAccPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, timeout=10)

    @allure.step('Нажать «Личный кабинет»')
    def click_personal_account(self):
        self.wait_page_ready()
        self.click(personal_locators.PERSONAL_ACCOUNT_LINK)

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

    @allure.step('Нажать «Выход»')
    def click_logout(self):
        self.wait_page_ready()
        self.click(personal_locators.LOGOUT_BUTTON)

    @allure.step('Дождаться редиректа на логин')
    def wait_login_opened(self):
        self.wait_page_ready()
        self.wait_url_contains('/login')
