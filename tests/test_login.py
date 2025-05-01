import pytest
from pages.login import LoginPage

def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "wrong_password")
    error_text = login_page.get_error_message()
    assert "Epic sadface" in error_text
