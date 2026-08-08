from playwright.sync_api import expect
class AddtocartPage:
    def __init__(self,page):
        self.addtoCartBtn = page.locator('input#add-to-cart-button')

    def clickOnAddToCartBtn(self):
        self.addtoCartBtn.click()

    