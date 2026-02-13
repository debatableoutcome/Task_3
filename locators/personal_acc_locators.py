
from selenium.webdriver.common.by import By


PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/account"]')

PROFILE_MENU_LINK = (By.CSS_SELECTOR, 'a[href="/account/profile"]')
ORDER_HISTORY_MENU_LINK = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')

LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выход")]')

PROFILE_TITLE = (By.XPATH, '//*[contains(text(), "Профиль")]')
ORDER_HISTORY_TITLE = (By.XPATH, '//*[contains(text(), "История заказов")]')
