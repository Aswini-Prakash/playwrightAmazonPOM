from playwright.sync_api import expect
class ResultPage:
    def __init__(self,page):
        self.page = page
        self.addTocartbtn = lambda product: page.locator(f'(//h2[contains(@aria-label,"{product}")]/ancestor::div[@data-component-type="s-search-result"]//input[@aria-label="Add to cart"])[1]')        
        self.cart_count = page.locator('span[id="nav-cart-count"]')
        #self.productlink = page.locator('//h2[contains(@aria-label,"{product}")]')
        self.booklink = page.locator('(//h2[contains(@aria-label,"We Are There For Each Other: An Intense Love Story of 4 Friends on a Road Trip of a Lifetime")])[1]')
        
    

    def clickOnAddToCartbtn(self,product):
        self.addTocartbtn(product).click()
    def validateCartCount(self):
        return int(self.cart_count.text_content())
    def clickOnProductlink(self):
        self.productlink.click()

    def open_product_page(self):
        with self.page.expect_popup() as popup_info:
            self.booklink.click()
        product_page = popup_info.value
        product_page.wait_for_load_state()
        return product_page

        
    

