import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.suite('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    def test_open_recovery_page(self, driver):
        page = ForgotPasswordPage(driver)

        page.open_page()

        assert '/forgot-password' in driver.current_url


    @allure.title('Ввод почты и клик по кнопке Восстановить')
    def test_enter_email_and_click_restore(self, driver):
        page = ForgotPasswordPage(driver)

        page.open_page()
        page.enter_email('test@test.ru')
        page.click_restore()

        assert '/reset-password' in driver.current_url


    @allure.title('Кнопка показать/скрыть пароль делает поле активным')
    def test_show_password_makes_field_active(self, driver):

        forgot = ForgotPasswordPage(driver)
        reset = ResetPasswordPage(driver)

        forgot.open_page()
        forgot.enter_email('test@test.ru')
        forgot.click_restore()

        reset.wait_for_page_ready()
        reset.click_show_hide_password()

        assert reset.password_field_is_active()
