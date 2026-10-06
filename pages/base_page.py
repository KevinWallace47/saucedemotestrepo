class BasePage:
    def __init__(self, page):
        self.page = page
    def navigate(self, path=""):
        self.page.goto(f"https://www.saucedemo.com/")

