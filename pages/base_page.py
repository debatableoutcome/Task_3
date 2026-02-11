from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def wait_overlay_gone(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(BaseLocators.MODAL_OVERLAY))
        except TimeoutException:
            pass

    def wait_clickable(self, locator):
        self.wait_overlay_gone()
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.wait_clickable(locator)
        element.click()

    def click_js(self, locator):
        self.wait_overlay_gone()
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].click();', element)

    def fill(self, locator, value):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
