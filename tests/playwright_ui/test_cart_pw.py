from playwright.sync_api import Page, expect

    
def test_add_to_cart(page: Page):
    page.add_locator_handler(
    page.locator("ins.adsbygoogle-noablate[data-vignette-loaded='true']").first,
    lambda ad: ad.evaluate("el => el.remove()"),
    )
    page.goto("https://automationexercise.com")
    page.get_by_role("link", name="Products").click()
    card = page.locator(".product-image-wrapper").filter(has_text="Blue Top")
    card.get_by_text("Add to cart").first.click()
