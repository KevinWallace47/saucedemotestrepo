from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("[data-test='checkout']")
        self.item_title = page.locator(".inventory_item_name")

    def proceed_to_checkout(self):
        self.checkout_button.click()