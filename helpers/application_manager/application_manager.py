from pages.home_page.domowebshop_home_page import DemowebshopHomePage
from pages.login_page.demowebshop_login_page import DemowebshopLoginPage


class ApplicationManager:

    def __init__(self):
        self.login_page = DemowebshopLoginPage()
        self.home_page = DemowebshopHomePage()


demowebshop_app = ApplicationManager()
