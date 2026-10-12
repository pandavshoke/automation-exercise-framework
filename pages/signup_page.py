from selenium.webdriver.common.by import By

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-name']").send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']").send_keys(email)

    def click_signup(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']").click()
