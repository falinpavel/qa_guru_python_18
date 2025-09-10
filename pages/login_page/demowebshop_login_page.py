import logging
import allure
import pytest
import requests

from selene import browser

from helpers.data.links import Links


class DemowebshopLoginPage:

    def __init__(self):
        self.url = Links.LOGIN_PAGE

    @allure.step("Login user with api")
    def login_user_with_api(self, cookie):
        with allure.step("Add auth cookie to browser"):
            browser.open(self.url)
            browser.driver.add_cookie(
                {
                    "name": "NOPCOMMERCE.AUTH",
                    "value": cookie
                }
            )
            browser.open(self.url)
