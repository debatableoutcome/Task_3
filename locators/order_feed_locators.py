from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_CARD = (By.CSS_SELECTOR, "li[class*='OrderHistory_listItem']")
    ORDER_CARD_LINK = (By.CSS_SELECTOR, "a[class*='OrderHistory_link']")
    ORDER_MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal']")
    ORDER_MODAL_OPENED = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
