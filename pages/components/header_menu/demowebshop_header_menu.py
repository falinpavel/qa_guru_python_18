import allure

from selene import browser, have, be
from selene.core.conditions import Condition as EC


class DemowebshopHeaderMenu:
    def click_on_group(self, group_name):
        with allure.step(f"Hover on group {group_name}"):
            browser.element(f"//ul[@class='top-menu']/li/a[text()='{group_name}']").should(
                EC.by_and(be.visible, have.text(group_name))).hover().click()
        return self
