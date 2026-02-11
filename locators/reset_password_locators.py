from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    SHOW_HIDE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon")
