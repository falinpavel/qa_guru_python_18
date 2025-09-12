import allure

from helpers.application_manager.application_manager import demowebshop_app
from helpers.data.products import Products


@allure.feature("Added product in catalog")
class TestAddedProductInCatalog:

    @allure.story("Added product in catalog with api and check product in cart ui")
    @allure.title("Added product in catalog with api and check product in cart with ui")
    def test_add_product_in_catalog_and_check_cart_icon(self, api_auth_session):
        session = api_auth_session
        demowebshop_app.login_page.login_user_with_api_session(session=session)
        demowebshop_app.home_page.open().is_opened()
        demowebshop_app.catalog_page.add_product_simple_computer_with_api(
            session=session,
            product_id=Products.simple_computer,
            quantity="1"
        )
