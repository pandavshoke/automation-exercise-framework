# Automation Exercise Framework

A learning project on test automation for the [Automation Exercise](https://automationexercise.com) website: UI tests built with Selenium and API tests built with `requests`, organized in a single pytest-based framework. The tests run in GitHub Actions on every push to `main`, and the results are saved as HTML reports.

## Tech stack

- Python, pytest
- Selenium WebDriver (Chrome, headless)
- requests
- pytest-rerunfailures, pytest-html
- Page Object pattern
- GitHub Actions

## Test coverage

7 tests in total.

**UI (4):**
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
.github/workflows/tests.yml   CI: test runs and report upload
pages/                        Page Objects: classes for the site's pages
tests/ui/                     UI tests, fixtures (conftest.py) and helpers.py
tests/api/                    API tests
requirements.txt              dependencies
```

## Running locally

Requires Python and an installed Chrome browser.

```
pip install -r requirements.txt
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

The `tests.yml` workflow runs on every push to `main` (Python 3.14, `ubuntu-latest`): it installs the dependencies, runs the UI tests, then the API tests. The API tests run even if the UI tests fail. After each test step the report is uploaded as a run artifact (`ui_test` and `api_test`), and you can download it from the run page in the Actions tab.

## Known limitations

- The tests run against a live public website, so they depend on its speed and availability. Failed tests are retried up to 2 times in CI, and the checkout test is also marked for retries locally.
- Each registration test creates a new user on the site with a random email.