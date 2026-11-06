from playwright.sync_api import Page, expect
from helpers_pw import add_product_and_go_to_cart_pw


def test_add_to_cart(page: Page):
    page.goto("https://automationexercise.com")
    add_product_and_go_to_cart_pw(page, "Blue Top")
    expect(page.get_by_text("Blue Top")).to_be_visible()


def test_add_and_remove_product_from_cart_pw(page: Page):
    page.goto("https://automationexercise.com")
    add_product_and_go_to_cart_pw(page, "Blue Top")
    expect(page.get_by_text("Blue Top")).to_be_visible()
    page.locator("a.cart_quantity_delete[data-product-id='1']").click()
    expect(page.get_by_text("Blue Top")).to_have_count(0)
    
def test_add_to_cart(page: Page):
    page.goto("https://automationexercise.com")
    add_product_and_go_to_cart_pw(page, "Blue Top")
    expect(page.get_by_text("Blue Top")).to_be_visible()

    
def test_add_and_remove_product_from_cart_pw(page: Page):
    page.goto("https://automationexercise.com")
    add_product_and_go_to_cart_pw(page, "Blue Top")
    expect(page.get_by_text("Blue Top")).to_be_visible()
    page.locator("a.cart_quantity_delete[data-product-id='1']").click()
    expect(page.get_by_text("Blue Top")).to_have_count(0)

