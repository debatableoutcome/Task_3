import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_acc_page import PersonalAccPage
from data.user_data import USER_DATA

BASE_URL = 'https://stellarburgers.education-services.ru'


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


@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def authorized_user(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    personal_page = PersonalAccPage(driver)

    main_page.open()

    personal_page.click_personal_account()  
    login_page.login(USER_DATA['EMAIL'], USER_DATA['PASSWORD']) 

    personal_page.click_personal_account()  
    personal_page.wait_profile_opened()

    return personal_page
