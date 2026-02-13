from selenium.webdriver.common.by import By


class BaseLocators:
    MODAL_BACKDROP = (By.CSS_SELECTOR, 'div.Modal_modal_overlay__x2ZCr')
    MODAL_SPINNER = (By.CSS_SELECTOR, 'img.Modal_modal__loading__3534A')
