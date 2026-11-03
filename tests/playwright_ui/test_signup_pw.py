from playwright.sync_api import Page, expect
import random


def test_signup_pw(page: Page):
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name=" Signup / Login").click()
    email = f"testuser{random.randint(1000, 9999)}@test.com"
    names = ["John", "Alice", "Anna", "Mike", "Sarah"]
    name = random.choice(names)
    page.locator("[data-qa='signup-name']").fill(name)
    page.locator("[data-qa='signup-email']").fill(email)
    page.locator("[data-qa='signup-button']").click()
    expect(page.locator("[data-qa='password']")).to_be_visible()
    