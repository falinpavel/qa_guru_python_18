import allure

from helpers.application_manager.application_manager import demowebshop_app


@allure.feature("Added product in catalog")
class TestAddedProductInCatalog:

    @allure.story("Added product in catalog with api and check product in cart ui")
    @allure.title("Added product in catalog with api and check product in cart with ui")
    def test_add_product_in_catalog_and_check_cart(self, api_auth_cookie):
        demowebshop_app.login_page.login_user_with_api(
            cookie=api_auth_cookie
        )
        demowebshop_app.catalog_page \
            .add_product_to_cart_with_api(cookie=api_auth_cookie, product_id="13/1/1") \
            .add_product_to_cart_with_api(cookie=api_auth_cookie, product_id="31/1/1") \
            .add_product_to_cart_with_api(cookie=api_auth_cookie, product_id="72/1/1") \
            .add_product_to_cart_with_api(cookie=api_auth_cookie, product_id="2/1/1")
