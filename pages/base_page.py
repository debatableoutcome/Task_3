import allure

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop as sele_drag_and_drop

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открыть страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Дождаться готовности страницы')
    def wait_page_ready(self):
        self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

    @allure.step('Дождаться, что URL содержит: {part}')
    def wait_url_contains(self, part):
        self.wait.until(EC.url_contains(part))

    @allure.step('Дождаться исчезновения оверлея/спиннера')
    def wait_overlay_gone(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(BaseLocators.MODAL_BACKDROP))
        except TimeoutException:
            pass

        try:
            self.wait.until(EC.invisibility_of_element_located(BaseLocators.MODAL_SPINNER))
        except TimeoutException:
            pass

    @allure.step('Дождаться кликабельности элемента: {locator}')
    def wait_clickable(self, locator):
        self.wait_overlay_gone()
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Клик по элементу: {locator}')
    def click(self, locator):
        element = self.wait_clickable(locator)
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.click_js(locator)

    @allure.step('Клик по элементу через JS: {locator}')
    def click_js(self, locator):
        self.wait_overlay_gone()
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].click();', element)

    @allure.step('Заполнить поле: {locator}')
    def fill(self, locator, value):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    @allure.step('Проверить, что элемент видим: {locator}')
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться присутствия элемента: {locator}')
    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Дождаться скрытия элемента: {locator}')
    def wait_not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент на элемент (seletools): {source_locator} -> {target_locator}')
    def drag_and_drop_on_element(self, source_locator, target_locator):
        self.wait_overlay_gone()
        source = self.wait_present(source_locator)
        target = self.wait_present(target_locator)
        sele_drag_and_drop(self.driver, source, target)

    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
