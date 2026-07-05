"""
cart_page.py
Page Object for the Cart page — used to verify products were added
correctly (name, price, quantity).
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    ITEM_QUANTITY = (By.CSS_SELECTOR, ".cart_quantity")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_item_count(self) -> int:
        return len(self.find_all(self.CART_ITEM))

    def get_item_names(self):
        return [el.text for el in self.find_all(self.ITEM_NAME)]

    def get_item_prices(self):
        return [el.text for el in self.find_all(self.ITEM_PRICE)]

    def is_cart_empty(self) -> bool:
        return not self.is_present(self.CART_ITEM)
