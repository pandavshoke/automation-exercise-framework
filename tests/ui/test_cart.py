import pytest
from pages.cart_page import CartPage
from helpers import add_product_and_go_to_cart

def test_add_and_remove_product_from_cart(driver, wait):
    add_product_and_go_to_cart(driver, wait, "1")
    cart_page = CartPage(driver)
    assert cart_page.is_product_in_cart("1")
    cart_page.remove_product("1")
    cart_page.wait_for_product_removed(wait, "1")
    assert not cart_page.is_product_in_cart("1")
