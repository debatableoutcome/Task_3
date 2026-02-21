import allure

from data.user_data import USER_DATA
from pages.personal_acc_page import PersonalAccPage


class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver):
        personal_page = PersonalAccPage(driver)
        personal_page.open_profile_as_authorized_user(USER_DATA['EMAIL'], USER_DATA['PASSWORD'])
        assert personal_page.current_url_contains('/account/profile')

    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver):
        personal_page = PersonalAccPage(driver)
        personal_page.open_profile_as_authorized_user(USER_DATA['EMAIL'], USER_DATA['PASSWORD'])
        personal_page.click_order_history()
        personal_page.wait_order_history_opened()

        assert personal_page.current_url_contains('/account/order-history')

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver):
        personal_page = PersonalAccPage(driver)
        personal_page.open_profile_as_authorized_user(USER_DATA['EMAIL'], USER_DATA['PASSWORD'])
        personal_page.click_logout()
        personal_page.wait_login_opened()

        assert personal_page.current_url_contains('/login')
