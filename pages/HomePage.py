import allure
from playwright.sync_api import expect
class Homepage:
    def __init__(self,page):
        self.loginbtn =  page.locator("//span[text()='Hello, sign in']")
        self.searchtxtbox = page.locator("//input[@id='twotabsearchtextbox']")
        self.searchbtn = page.locator("#nav-search-submit-button")
        self.retursAndOrederLink = page.locator('//a[@data-nav-role="signin"]')
        
    @allure.step("validateVisibilityOfSignIn")
    def validateVisibilityOfSignIn(self):
        expect(self.loginbtn).to_be_visible()
    @allure.step("validateVisibilityOfSignIn")
    def clickOnSignin(self):
        self.loginbtn.click()
    @allure.step("validateVisibilityOfSignIn")    
    def enterSearchProduct(self,product):
        self.searchtxtbox.fill(product)
    def clickOnSearch(self):
        self.searchbtn.click()
    def clickOnAddToCart(self):
        self.addTocartbtn.click()
