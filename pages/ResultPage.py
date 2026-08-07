from playwright.sync_api import expect
class ResultPage:
    def __init__(self,page):
        
        self.addTocartbtn = page.locator('//h2[@aria-label="Sponsored Ad - Crompton 20 W Standard B22 LED Bulb (White)"]/ancestor::div[@data-component-type="s-search-result"]//input[@aria-label="Add to cart"]')
        self.cart_count = page.locator('span[id="nav-cart-count"]')
        
    

    def clickOnAddToCart(self):
        self.addTocartbtn.click()
    def validateCartCount(self):
        return int(self.cart_count.text_content())
    

