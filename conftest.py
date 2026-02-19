import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    driver.set_window_size(1280, 720)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
