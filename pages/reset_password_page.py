import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step('Дождаться открытия страницы сброса пароля')
    def wait_for_page_ready(self):
        self.is_visible(ResetPasswordLocators.PASSWORD_INPUT)
        self.wait.until(EC.url_contains('/reset-password'))

    @allure.step('Нажать показать/скрыть пароль')
    def click_show_hide_password(self):
        self.click_js(ResetPasswordLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('Проверить, что поле пароля активно')
    def password_field_is_active(self):
        el = self.is_visible(ResetPasswordLocators.PASSWORD_INPUT)
        return el.get_attribute('type') == 'text'
