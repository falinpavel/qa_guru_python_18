import logging
import allure
import pytest
import requests

from selene import browser
from selenium.webdriver.chrome.options import Options

from helpers.data.links import Links
from helpers.data.user import User


@pytest.fixture(
    scope="function",
    autouse=True
)
def browser_configurate():
    chrome_options = Options()
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = chrome_options

    yield browser.quit()


@pytest.fixture(scope="session")
def api_auth_session():
    session = requests.Session()

    with allure.step("Send request POST for login with credentials"):
        response = session.post(
            url=Links.LOGIN_PAGE,
            data={
                "Email": User.USER_LOGIN,
                "Password": User.USER_PASSWORD
            },
            allow_redirects=False
        )

        logging.info(f"Status code: {response.status_code}")
        logging.info(f"Session cookies: {session.cookies.get_dict()}")

        assert response.status_code == 302
        assert "NOPCOMMERCE.AUTH" in session.cookies.get_dict()

        yield session
