from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class AccountInfoPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='password']").send_keys(password)

    def click_create_account(self, wait):
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='create-account']")))
        self.driver.execute_script("arguments[0].click();", element)

    def select_day(self, days):
        select_element = Select(self.driver.find_element(By.CSS_SELECTOR, "[data-qa='days']"))
        select_element.select_by_value(days)

    def select_month(self, months):
        select_element = Select(self.driver.find_element(By.CSS_SELECTOR,"[data-qa='months']" ))
        select_element.select_by_value(months)

    def select_year(self, years):
        select_element = Select(self.driver.find_element(By.CSS_SELECTOR, "[data-qa='years']"))
        select_element.select_by_value(years)

    def select_country(self, country):
        select_element = Select(self.driver.find_element(By.CSS_SELECTOR, "[data-qa='country']"))
        select_element.select_by_visible_text(country)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='first_name']").send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='last_name']").send_keys(last_name)

    def enter_address(self, address):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='address']").send_keys(address)

    def enter_state(self, state):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='state']").send_keys(state)

    def enter_city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='city']").send_keys(city)

    def enter_zipcode(self, zipcode):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='zipcode']").send_keys(zipcode)

    def enter_mobile_number(self, mobile_number):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='mobile_number']").send_keys(mobile_number)

    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']").click()