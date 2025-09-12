import allure

from selene import browser

from helpers.data.links import Links


class DemowebshopCartPage:
    def __init__(self):
        self.url = Links.CART_PAGE

    def open(self):
        with allure.step("Open cart page"):
            browser.open(self.url)
        return self
    