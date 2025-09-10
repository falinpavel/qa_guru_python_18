import allure

from helpers.application_manager.application_manager import demowebshop_app
from helpers.data.user import User


@allure.feature("Login user")
class TestLoginUser:

    @allure.story("Login user with api")
    @allure.title("Login user with api and check user is logged in ui")
    def test_login_user_with_api(self, api_auth_cookie):
        demowebshop_app.login_page.login_user_with_api(
            cookie=api_auth_cookie
        )
        demowebshop_app.home_page \
            .open() \
            .is_opened() \
            .check_user_is_logged_in(user_login=User.USER_LOGIN)

