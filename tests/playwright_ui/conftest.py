import pytest

@pytest.fixture(autouse=True)
def close_ads(page):
    page.add_locator_handler(
    page.locator("ins.adsbygoogle-noablate[data-vignette-loaded='true']").first,
    lambda ad: ad.evaluate("el => el.remove()"),
    )
