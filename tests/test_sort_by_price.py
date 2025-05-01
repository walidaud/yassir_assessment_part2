from pages.login import LoginPage
from pages.inventory import InventoryPage

def test_sort_products_by_price_low_to_high(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.sort_by("lohi")  # "lohi" = low to high

    prices = inventory_page.get_all_prices()
    sorted_prices = sorted(prices)
    assert prices == sorted_prices, "Prices are not sorted in ascending order"
