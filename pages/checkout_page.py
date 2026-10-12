from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_comment(self, comment):
        self.driver.find_element(By.CSS_SELECTOR, "textarea[name='message']").send_keys(comment)

    def click_place_order(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/payment']").click()
