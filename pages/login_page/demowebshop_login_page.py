import requests

from selene import browser

from helpers.data.links import Links
from helpers.data.user import User


class DemowebshopLoginPage:

    def __init__(self):
        self.url = Links.LOGIN_PAGE

    def api_login_user(self, user_login, user_password):
        response = requests.post(
            url=self.url,
            json={
                "Email": user_login,
                "Password": user_password
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
