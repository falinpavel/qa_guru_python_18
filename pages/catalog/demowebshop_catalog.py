import logging

import allure
import requests

from helpers.data.links import Links


class DemowebshopCatalogPage:

    def __init__(self):
        self.url = Links.HOME_PAGE

    @allure.step("Add product to cart with api")
    def add_product_to_cart_with_api(self, cookie, product_id):
        with allure.step("Add product to cart with api"):
            response = requests.post(
                url=f"{self.url}addproducttocart/catalog/{product_id}",
                headers={
                    "Cookie": cookie
                }
            )
            allure.attach(
                body=response.text,
                name="Response body",
                attachment_type=allure.attachment_type.TEXT,
                extension="json"
            )
            logging.info(response.status_code)
            logging.info(response.text)
            assert response.status_code == 200
        return self
