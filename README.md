# Automation Exercise Framework

A learning project on test automation for the [Automation Exercise](https://automationexercise.com) website: UI tests built with both Selenium and Playwright, plus API tests built with requests, organized in a single pytest-based framework. The tests run in GitHub Actions on every push to `main`, and the results are saved as HTML reports.

## Tech stack

- Python, pytest
- Selenium WebDriver (Chrome, headless)
- Playwright (via pytest-playwright)
- requests
- pytest-rerunfailures, pytest-html
- Page Object pattern (Selenium tests)
- GitHub Actions

## Test coverage

11 tests in total: 7 distinct scenarios, with the 4 UI scenarios implemented twice (Selenium and Playwright) for comparison, plus 3 API tests.

**UI scenarios(4) implemented in both Selenium and Playwright:**
- adding a product to the cart;
- adding and removing a product in the cart;
- full registration of a new account;
- checkout flow: from adding a product and registering to the payment page.

**API (3):**
- getting the product list (`productsList`);
- searching for a product (`searchProduct`);
- negative scenario: a wrong request method for `productsList` returns code 405.

## Project structure

```
.github/workflows/tests.yml    CI: Selenium, API and Playwright runs, report upload
pages/                         Page Objects for the Selenium tests
tests/ui/                      Selenium UI tests, fixtures (conftest.py), helpers.py
tests/playwright_ui/           Playwright UI tests (same scenarios), conftest.py, helpers_pw.py
tests/api/                     API tests
requirements.txt               dependencies
```

## Running locally

Requires Python and an installed Chrome browser.

```
pip install -r requirements.txt
playwright install chromium
pytest
```

UI or API tests only:

```
pytest tests/ui
pytest tests/api
```

With an HTML report:

```
pytest --html=report.html --self-contained-html
```

## CI

The `tests.yml` workflow runs on every push to `main` (Python 3.14, `ubuntu-latest`): it installs the dependencies, runs the UI tests, API tests then the playwright tests. The API and Playwright steps run even if an earlier step fails. After each test step the report is uploaded as a run artifact (`ui_test`, `api_test` and `playwright_test`), and you can download it from the run page in the Actions tab.

## Known limitations

- The tests run against a live public website, so they depend on its speed and availability. Failed tests are retried up to 2 times in CI, and the checkout test is also marked for retries locally.(Selenium)
- The site shows third-party ads (Google ad overlays) at random. They can cover buttons and they can also mark the page as `aria-hidden`, which makes role-based Playwright locators fail to find elements that are visible on screen. The Playwright tests handle this with an autouse fixture in `conftest.py` that removes the ad overlay, and use CSS selectors where role-based search is unreliable.
- Each registration test creates a new user on the site with a unique, UUID-based email.