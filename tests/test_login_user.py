from helpers.application_manager.application_manager import demowebshop_app
from helpers.data.user import User


class TestLoginUser:
    def test_login_user_with_api(self):
        demowebshop_app.login_page.api_login_user()
        demowebshop_app.home_page \
            .open() \
            .is_opened() \
            .check_user_is_logged_in(user_login=User.USER_LOGIN)

