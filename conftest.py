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
    yield
    browser.quit()


@pytest.fixture(scope="session")
def api_auth_cookie():
    with allure.step("Send request POST for login with credentials"):
        response = requests.post(
            url=Links.LOGIN_PAGE,
            json={
                "Email": User.USER_LOGIN,
                "Password": User.USER_PASSWORD
            },
            allow_redirects=False
        )
        logging.info(response.request.body)
        logging.info(response.status_code)
        allure.attach(
            body=response.request.body,
            name="Request body",
            attachment_type=allure.attachment_type.JSON,
            extension="json"
        )
        allure.attach(
            body=response.text,
            name="Response body",
            attachment_type=allure.attachment_type.TEXT,
            extension="json"
        )

    with allure.step("Get auth cookie from response"):
        assert response.status_code == 302
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        allure.attach(
            body=cookie,
            name="Auth cookie",
            attachment_type=allure.attachment_type.TEXT,
            extension="json"
        )
        allure.attach(
            body=str(response.cookies),
            name="All cookies",
            attachment_type=allure.attachment_type.TEXT,
            extension="json"
        )
        yield cookie
