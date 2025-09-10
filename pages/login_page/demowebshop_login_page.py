import logging
import allure
import requests

from selene import browser

from helpers.data.links import Links


class DemowebshopLoginPage:

    def __init__(self):
        self.url = Links.LOGIN_PAGE

    @allure.step("Login user with api")
    def api_login_user(self, user_login, user_password):
        with allure.step("Send request POST for login with credentials"):
            response = requests.post(
                url=self.url,
                json={
                    "Email": user_login,
                    "Password": user_password
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
        with allure.step("Add auth cookie to browser"):
            browser.open(self.url)
            browser.driver.add_cookie(
                {
                    "name": "NOPCOMMERCE.AUTH",
                    "value": cookie
                }
            )
            browser.open(self.url)
