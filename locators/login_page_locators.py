from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
