import requests

from selene import browser, have, be
from selene.core.conditions import Condition as EC

from helpers.data.links import Links


class DemowebshopHomePage:

    def __init__(self):
        self.url = Links.HOME_PAGE

    def open(self):
        browser.open(self.url)
        return self

    def is_opened(self):
        browser.should(have.url(self.url))
        browser.element("//h2[@class='topic-html-content-header']").should(
            EC.by_and(be.visible, have.text("Welcome to our store")))
        return self

    def check_user_is_logged_in(self, user_login):
        browser.element("div[class='header-links'] a[class='account']").should(
            EC.by_and(be.visible, have.text(user_login)))
        return self
