import logging
import allure

from helpers.data.links import Links


class DemowebshopCatalogPage:

    def __init__(self):
        self.url = Links.HOME_PAGE

    @allure.step("Add product to cart with api")
    def add_product_simple_computer_with_api(self, session, product_id, quantity):
        with allure.step("Add product to cart with api"):
            response = session.post(
                url=f"{self.url}/addproducttocart/details/{product_id}",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest"
                },
                data={
                    "product_attribute_75_5_31": "96",
                    "product_attribute_75_6_32": "99",
                    "product_attribute_75_3_33": "103",
                    "product_attribute_75_8_35": "108",
                    "addtocart_75.EnteredQuantity": quantity
                },
                allow_redirects=False
            )

            logging.info(response.status_code)
            logging.info(response.text)
            assert response.status_code == 200
        return self

    @allure.step("Add product to cart with api")
    def add_product_women_top_with_api(self, session, product_id, quantity):
        with allure.step("Add product to cart with api"):
            response = session.post(
                url=f"{self.url}/addproducttocart/details/{product_id}",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest"
                },
                data={
                    "product_attribute_5_7_1": "3",
                    "addtocart_5.EnteredQuantity": quantity
                },
                allow_redirects=False
            )

            logging.info(response.status_code)
            logging.info(response.text)
            assert response.status_code == 200
        return self
