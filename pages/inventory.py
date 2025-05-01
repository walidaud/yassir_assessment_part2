from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def sort_by(self, sort_option):
        # sort_option: 'az', 'za', 'lohi', 'hilo'
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value(sort_option)

    def get_all_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(el.text.replace("$", "")) for el in price_elements]
