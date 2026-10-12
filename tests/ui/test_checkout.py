from helpers import add_product_and_go_to_cart
from helpers import register_new_account
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
import pytest

@pytest.mark.flaky(reruns=2)
def test_checkout_flow(driver, wait):
    add_product_and_go_to_cart(driver, wait, "1")
    cart_page = CartPage(driver)
    cart_page.click_proceed_to_checkout()
    home_page = HomePage(driver)
    home_page.click_signup_login()
    register_new_account(driver, wait)
    home_page.click_cart()
    cart_page.click_proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_comment("Aa_/123/Bb*&")
    checkout_page.click_place_order()
    assert "payment" in driver.current_url

