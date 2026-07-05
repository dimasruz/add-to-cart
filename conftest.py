"""
conftest.py
Shared fixtures available to all test files automatically (no import needed).
"""

import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"

# Standard demo credentials provided by saucedemo.com for automation practice
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


def pytest_addoption(parser):
    """Allows running: pytest --headless"""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless browser mode",
    )


@pytest.fixture
def driver(request):
    """Creates a fresh browser instance for each test, and quits it after."""
    headless = request.config.getoption("--headless")
    driver = get_driver(headless=headless)
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Returns a driver already logged in and on the Inventory page."""
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver
