"""
test_add_to_cart.py
Test suite covering the "Add to Cart" functionality on saucedemo.com.
"""

import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


# A few representative products (id, display name) used across tests
BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"
BOLT_TSHIRT = "sauce-labs-bolt-t-shirt"


@pytest.mark.smoke
def test_add_single_product_to_cart(logged_in_driver):
    """TC01: Adding one product should update the cart badge to 1."""
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_product_to_cart(BACKPACK)

    assert inventory_page.get_cart_badge_count() == 1


@pytest.mark.regression
def test_add_multiple_products_to_cart(logged_in_driver):
    """TC02: Adding several distinct products should increment the badge for each one."""
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_product_to_cart(BACKPACK)
    inventory_page.add_product_to_cart(BIKE_LIGHT)
    inventory_page.add_product_to_cart(BOLT_TSHIRT)

    assert inventory_page.get_cart_badge_count() == 3


@pytest.mark.smoke
def test_cart_badge_updates_correctly(logged_in_driver):
    """TC03: Cart badge count should reflect exact number of items added, one at a time."""
    inventory_page = InventoryPage(logged_in_driver)

    assert inventory_page.get_cart_badge_count() == 0

    inventory_page.add_product_to_cart(BACKPACK)
    assert inventory_page.get_cart_badge_count() == 1

    inventory_page.add_product_to_cart(BIKE_LIGHT)
    assert inventory_page.get_cart_badge_count() == 2


@pytest.mark.regression
def test_button_changes_to_remove_after_adding(logged_in_driver):
    """TC04: 'Add to Cart' button should switch to 'Remove' once item is in the cart."""
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_product_to_cart(BACKPACK)

    assert inventory_page.is_remove_button_visible(BACKPACK) is True


@pytest.mark.regression
def test_remove_product_from_cart(logged_in_driver):
    """TC05: Removing a product should decrement the badge count back down."""
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_product_to_cart(BACKPACK)
    inventory_page.add_product_to_cart(BIKE_LIGHT)
    assert inventory_page.get_cart_badge_count() == 2

    inventory_page.remove_product_from_cart(BACKPACK)

    assert inventory_page.get_cart_badge_count() == 1


@pytest.mark.regression
def test_product_details_correct_in_cart(logged_in_driver):
    """TC06: The product added on the inventory page should appear in the cart
    with a matching name."""
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_product_to_cart(BACKPACK)

    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_driver)

    assert cart_page.get_cart_item_count() == 1
    assert "Sauce Labs Backpack" in cart_page.get_item_names()


@pytest.mark.regression
@pytest.mark.parametrize(
    "product_id",
    [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)",
    ],
)
def test_add_to_cart_for_each_product(logged_in_driver, product_id):
    """TC07: Data-driven test — every individual product on the page
    can be added to the cart successfully."""
    inventory_page = InventoryPage(logged_in_driver)

    inventory_page.add_product_to_cart(product_id)

    assert inventory_page.get_cart_badge_count() == 1
    assert inventory_page.is_remove_button_visible(product_id) is True
