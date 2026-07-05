"""
Handles creation of the Selenium WebDriver instance.
Keeping this logic separate from conftest.py makes it easy to
swap browsers or add remote/grid execution later.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_driver(headless: bool = False):
    """Create and return a configured Chrome WebDriver instance."""
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    return driver
