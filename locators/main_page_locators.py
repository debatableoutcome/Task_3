from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/account"]')
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
