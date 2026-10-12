from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_login(self):
        element = self.driver.find_element(By.CSS_SELECTOR,"a[href='/login']")
        self.driver.execute_script("arguments[0].click();", element)

    def click_products(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()

    def click_cart(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
        self.driver.execute_script("arguments[0].click();", element)