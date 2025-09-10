import allure
import requests

from selene import browser, have, be
from selene.core.conditions import Condition as EC

from helpers.data.links import Links


class DemowebshopHomePage:

    def __init__(self):
        self.url = Links.HOME_PAGE

    @allure.step("Open home page")
    def open(self):
        with allure.step(f"Open home page {self.url}"):
            browser.open(self.url)
        return self

    @allure.step("Check home page is opened")
    def is_opened(self):
        with allure.step("Check url"):
            browser.should(have.url(self.url))
        with allure.step("Should see welcome message"):
            browser.element("//h2[@class='topic-html-content-header']").should(
                EC.by_and(be.visible, have.text("Welcome to our store")))
        return self

    @allure.step("Check user is logged in")
    def check_user_is_logged_in(self, user_login):
        with allure.step("Check username in header menu"):
            browser.element("div[class='header-links'] a[class='account']").should(
                EC.by_and(be.visible, have.text(user_login)))
        return self
