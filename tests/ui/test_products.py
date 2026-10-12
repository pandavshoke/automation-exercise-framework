import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
def test_add_to_cart(driver, wait):
    home_page = HomePage(driver)
    home_page.click_products()
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart("1")
    products_page.wait_for_product_added(wait)