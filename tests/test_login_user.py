from helpers.application_manager.application_manager import demowebshop_app
from helpers.data.user import User
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Authorization",
    feature="Authorization users"
)
class TestLoginUser:

    @allure_mid_level_marks(
        story="Authorization user and set cookies",
        testcase_id="TC_02",
        title="Authorization user and check user is logged in ui",
        label='UI + API',
        owner="AQA Falin Pavel"
    )
    def test_login_user_with_api(self, api_auth_session):
        demowebshop_app.login_page.login_user_with_api_session(session=api_auth_session)
        demowebshop_app.home_page \
            .open() \
            .is_opened() \
            .check_user_is_logged_in(user_login=User.USER_LOGIN)
