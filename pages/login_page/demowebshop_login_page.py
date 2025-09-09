import requests

from selene import browser

from helpers.data.links import Links
from helpers.data.user import User


class DemowebshopLoginPage:

    def __init__(self):
        self.url = Links.LOGIN_PAGE
        self.user_login = User.USER_LOGIN
        self.user_password = User.USER_PASSWORD

    def api_login_user(self):
        response = requests.post(
            url=self.url,
            json={
                "Email": self.user_login,
                "Password": self.user_password
            },
            allow_redirects=False
        )
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")
        assert response.status_code == 302
        browser.open(self.url)
        browser.driver.add_cookie(
            {
                "name": "NOPCOMMERCE.AUTH",
                "value": cookie
            }
        )
        browser.open(self.url)
