from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/ancestor::a")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")
