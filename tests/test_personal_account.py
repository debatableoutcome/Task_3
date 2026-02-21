import allure

from data.user_data import USER_DATA
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_acc_page import PersonalAccPage


class TestPersonalAccount:
    @staticmethod
    def _open_personal_account_as_authorized_user(driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_page = PersonalAccPage(driver)

        main_page.open()
        personal_page.click_personal_account()
        login_page.login(USER_DATA['EMAIL'], USER_DATA['PASSWORD'])
        personal_page.click_personal_account()
        personal_page.wait_profile_opened()
        return personal_page

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        personal_page = self._open_personal_account_as_authorized_user(driver)
        assert personal_page.current_url_contains('/account/profile')

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver):
        personal_page = self._open_personal_account_as_authorized_user(driver)
        personal_page.click_order_history()
        personal_page.wait_order_history_opened()

        assert personal_page.current_url_contains('/account/order-history')

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver):
        personal_page = self._open_personal_account_as_authorized_user(driver)
        personal_page.click_logout()
        personal_page.wait_login_opened()

        assert personal_page.current_url_contains('/login')
