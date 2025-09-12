import allure

from selene import browser, be, by, command, have
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
            browser.element(f"//a[@class='product-name' and text()='{product_name}']").should(
                EC.by_and(be.visible, have.text(product_name)))
