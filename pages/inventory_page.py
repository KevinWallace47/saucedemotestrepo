from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.backpack_add_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def go_to_cart(self):
        self.cart_icon.click()