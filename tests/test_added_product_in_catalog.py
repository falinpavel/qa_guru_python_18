from helpers.application_manager.application_manager import demowebshop_app
from helpers.data.products import Products
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Catalog",
    feature="Added product in catalog and check product in cart"
)
class TestAddedProductInCatalog:

    @allure_mid_level_marks(
        story="Added product in catalog",
        testcase_id="TC_01",
        title="User add product in catalog and check product in cart",
        label='UI + API',
        owner="AQA Falin Pavel"
    )
    def test_add_product_in_catalog_and_check_cart_icon(self, api_auth_session):
        session = api_auth_session
        demowebshop_app.login_page.login_user_with_api_session(session=session)
        demowebshop_app.home_page.open().is_opened()
        demowebshop_app.catalog_page.add_product_simple_computer_with_api(
            session=session,
            product_id=Products.simple_computer,
            quantity="1"
        )
