from pages.components.header_menu.demowebshop_header_menu import DemowebshopHeaderMenu
from pages.home_page.demowebshop_home_page import DemowebshopHomePage
from pages.login_page.demowebshop_login_page import DemowebshopLoginPage


class ApplicationManager:

    def __init__(self):
        self.login_page = DemowebshopLoginPage()
        self.home_page = DemowebshopHomePage()
        self.header_menu = DemowebshopHeaderMenu()


demowebshop_app = ApplicationManager()
