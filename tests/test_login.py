import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_successful_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()

def test_locked_out_user(page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    