import pytest
import random
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage

def test_signup_full_flow(driver, wait):    
    assert "Automation" in driver.title
    home_page = HomePage(driver)
    home_page.click_signup_login()
    signup_page = SignupPage(driver)
    email = f"testuser{random.randint(1000, 9999)}@test.com"
    names = ["John", "Alice", "Anna", "Mike", "Sarah"]
    name = random.choice(names)
    signup_page.enter_name(name)
    signup_page.enter_email(email)
    signup_page.click_signup()
    account_info_page = AccountInfoPage(driver)
    account_info_page.wait_for_password(wait)
    account_info_page.enter_password("Test1234")
    account_info_page.select_day("30") 
    account_info_page.select_month("9")
    account_info_page.select_year("1984") 
    account_info_page.select_country("Canada")
    account_info_page.enter_first_name(name)
    account_info_page.enter_last_name("Smith")
    account_info_page.enter_address("10305 154 Ave")
    account_info_page.enter_state("Alberta (AB)")
    account_info_page.enter_city("Grande Prairie")
    account_info_page.enter_zipcode("T8X 0J6")
    account_info_page.enter_mobile_number("+1 (416) 555-0148")
    account_info_page.click_create_account(wait)
    assert "account_created" in driver.current_url