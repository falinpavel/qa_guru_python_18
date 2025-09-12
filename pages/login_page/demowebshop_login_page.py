import logging
import allure

from selene import browser

from helpers.data.links import Links


class DemowebshopLoginPage:

    def __init__(self):
        self.url = Links.LOGIN_PAGE

    @allure.step("Login user with api session")
    def login_user_with_api_session(self, session):
        with allure.step("Add all cookies from session to browser"):
            browser.open(self.url)

            cookies_dict = session.cookies.get_dict()
            logging.info(f"Adding cookies to browser: {cookies_dict}")

            for cookie_name, cookie_value in cookies_dict.items():
                browser.driver.add_cookie({
                    "name": cookie_name,
                    "value": cookie_value,
                    "domain": "demowebshop.tricentis.com"
                })
            browser.driver.refresh()
