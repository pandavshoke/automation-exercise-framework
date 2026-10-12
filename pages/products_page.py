from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_id):
        element = self.driver.find_element(By.CSS_SELECTOR, f"a[data-product-id='{product_id}']")
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_product_added(self, wait):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-title")))

    def close_modal(self, wait):
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.close-modal")))
        self.driver.execute_script("arguments[0].click();", element)
