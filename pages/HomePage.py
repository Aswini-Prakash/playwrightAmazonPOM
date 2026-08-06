from playwright.sync_api import expect
class Homepage:
    def __init__(self,page):
        self.loginbtn =  page.locator("//span[text()='Hello, sign in']")
        self.searchtxtbox = page.locator("//input[@id='twotabsearchtextbox']")
        self.searchbtn = page.locator("#nav-search-submit-button")
        




    def validateVisibilityOfSignIn(self):
        expect(self.loginbtn).to_be_visible()
    def clickOnSignin(self):
        self.loginbtn.click()
    def enterSearchProduct(self,product):
        self.searchtxtbox.fill(product)
    def clickOnSearch(self):
        self.searchbtn.click()
    def clickOnAddToCart(self):
        self.addTocartbtn.click()
