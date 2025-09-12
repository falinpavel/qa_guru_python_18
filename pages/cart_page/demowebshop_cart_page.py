import allure

from selene import browser, have, be
from selene.core.conditions import Condition as EC

from helpers.data.links import Links


class DemowebshopCartPage:
    def __init__(self):
        self.url = Links.CART_PAGE

    @allure.step("Open cart page")
    def open(self):
        with allure.step(f"Open cart page: {self.url}"):
            browser.open(self.url)
        return self

    @allure.step("Check added product in cart")
    def check_product_in_cart(self, product_name):
        with allure.step(f"Check product {product_name}"):
            browser.all(".product-name").should(EC.by_and(have.text(product_name)))
