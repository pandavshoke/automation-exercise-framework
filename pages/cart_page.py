from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_product_in_cart(self, product_id):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"a[href='/product_details/{product_id}']")
        return len(elements) > 0
        
    def remove_product(self, product_id):
        self.driver.find_element(By.CSS_SELECTOR, f"a[data-product-id='{product_id}'].cart_quantity_delete").click()

    def wait_for_product_removed(self, wait, product_id):
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, f"a[href='/product_details/{product_id}']")))

    def click_proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, ".check_out").click()