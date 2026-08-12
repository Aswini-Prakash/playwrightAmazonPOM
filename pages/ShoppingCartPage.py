from playwright.sync_api import expect

class ShoppingCartPage:
    def __init__(self,page):
        self.cartIcon = page.locator('//span[@class="nav-cart-icon nav-sprite"]')
        self.incrementcartIcon = page.locator('//span[@data-a-selector="increment-icon"]')
        self.subitemsMSg = page.locator('//span[@id="sc-subtotal-label-activecart"]')



    def clickOnCartIcon(self):
        self.cartIcon.click()
    def clickOnIncrementCartIcon(self):
        self.incrementcartIcon.click()
    def validateSubItemsMsg(self):
        return self.subitemsMSg.text_content().strip()
    
