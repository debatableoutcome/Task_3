from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(),'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
