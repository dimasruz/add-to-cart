"""
inventory_page.py
Page Object for the product listing ("Inventory") page — this is where
the core Add to Cart functionality lives.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")

    def _add_to_cart_button_locator(self, product_id: str):
        return (By.ID, f"add-to-cart-{product_id}")

    def _remove_button_locator(self, product_id: str):
        return (By.ID, f"remove-{product_id}")

    def add_product_to_cart(self, product_id: str):
        """
        product_id example: 'sauce-labs-backpack'
        (saucedemo button IDs follow the pattern add-to-cart-<product-slug>)
        """
        self.click(self._add_to_cart_button_locator(product_id))

    def remove_product_from_cart(self, product_id: str):
        self.click(self._remove_button_locator(product_id))

    def is_remove_button_visible(self, product_id: str) -> bool:
        return self.is_present(self._remove_button_locator(product_id))

    def get_cart_badge_count(self) -> int:
        """Returns 0 if the badge isn't showing (empty cart)."""
        if self.is_present(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def get_all_product_names(self):
        elements = self.find_all(self.ITEM_NAME)
        return [el.text for el in elements]

    def add_all_products_to_cart(self):
        """Adds every product currently listed on the inventory page."""
        buttons = self.find_all((By.CSS_SELECTOR, "button.btn_inventory"))
        for button in buttons:
            button.click()
