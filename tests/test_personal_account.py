import allure


class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, authorized_user):
        assert '/account/profile' in authorized_user.driver.current_url



    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver, authorized_user):
        authorized_user.click_order_history()
        authorized_user.wait_order_history_opened()

        assert '/account/order-history' in driver.current_url


    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, authorized_user):
        authorized_user.click_logout()
        authorized_user.wait_login_opened()

        assert '/login' in driver.current_url
