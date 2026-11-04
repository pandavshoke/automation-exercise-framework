import random
import re
from playwright.sync_api import Page

def register_new_account_pw(page: Page):
        email = f"testuser{random.randint(1000, 9999)}@test.com"
        names = ["John", "Alice", "Anna", "Mike", "Sarah"]
        name = random.choice(names)
        page.locator("[data-qa='signup-name']").fill(name)
        page.locator("[data-qa='signup-email']").fill(email)
        page.locator("[data-qa='signup-button']").click()
        page.locator("[data-qa='password']").fill("Test1234")
        page.locator("[data-qa='days']").select_option(value="30")
        page.locator("[data-qa='months']").select_option(value="9")
        page.locator("[data-qa='years']").select_option(value="1984")
        page.locator("[data-qa='first_name']").fill(name)
        page.locator("[data-qa='last_name']").fill("Smith")
        page.locator("[data-qa='address']").fill("10305 154 Ave")
        page.locator("[data-qa='country']").select_option(label="Canada")
        page.locator("[data-qa='state']").fill("Alberta (AB)")
        page.locator("[data-qa='city']").fill("Grande Prairie")
        page.locator("[data-qa='zipcode']").fill("T8X 0J6")
        page.locator("[data-qa='mobile_number']").fill("+1 (416) 555-0148")
        page.locator("[data-qa='create-account']").click()
