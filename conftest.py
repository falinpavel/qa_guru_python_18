import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options


@pytest.fixture(
    scope="function",
    autouse=True
)
def browser_configurate():
    chrome_options = Options()
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--window-size=1920,1080")
    browser.config.driver_options = chrome_options
    yield
    browser.quit()


