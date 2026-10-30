from playwright.sync_api import Page, expect

    
def test_add_to_cart(page: Page):
    page.goto("https://automationexercise.com")
    page.get_by_role("link", name="Products").click()
    card = page.locator(".product-image-wrapper").filter(has_text="Blue Top")
    card.get_by_text("Add to cart").first.click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
def test_add_and_remove_product_from_cart_pw(page: Page):
    page.goto("https://automationexercise.com")
    page.get_by_role("link", name="Products").click()
    card = page.locator(".product-image-wrapper").filter(has_text="Blue Top")
    card.get_by_text("Add to cart").first.click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.get_by_text("Blue Top")).to_be_visible()
    page.locator("a.cart_quantity_delete[data-product-id='1']").click()
    expect(page.get_by_text("Blue Top")).to_have_count(0)