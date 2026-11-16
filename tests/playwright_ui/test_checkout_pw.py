from playwright.sync_api import Page, expect
import re
from helpers_pw import add_product_and_go_to_cart_pw, register_new_account_pw


def test_checkout_pw(page: Page):
    page.goto("https://automationexercise.com")
    add_product_and_go_to_cart_pw(page, "Blue Top")
    page.locator(".check_out").click()
    page.get_by_role("link", name="Register / Login").click()
    register_new_account_pw(page)
    page.locator("[data-qa='continue-button']").click()
    page.get_by_role("link", name="Cart").click()
    page.locator(".check_out").click()
    page.locator("textarea[name='message']").fill("Aa_/123/Bb*&")
    page.locator("a[href='/payment']").click()
    expect(page).to_have_url(re.compile("payment"))

