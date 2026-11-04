from playwright.sync_api import Page, expect
import re
from helpers_pw import register_new_account_pw


def test_signup_pw(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name=" Signup / Login").click()
    register_new_account_pw(page)
    expect(page).to_have_url(re.compile("account_created"))
    