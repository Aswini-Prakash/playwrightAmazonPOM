from playwright.sync_api import sync_playwright,expect,Page

from pages.HomePage import Homepage
from pages.LoginPage import Loginpage

def test_validate_Authentication(page: Page,navigate_to_amazon):
        homePageObj= Homepage(page)
        loginPageObj= Loginpage(page)

        homePageObj.validateVisibilityOfSignIn()
        homePageObj.clickOnSignin()
        loginPageObj.validateVisibilityOfEmailTxtBox()
        loginPageObj.login("aswiniprakashan999@gmail.com","Aswini@123")
        expect(page.get_by_text("Hello, Aswini")).to_be_visible()
        

# def test_invalidate_Authentication(page: Page,navigate_to_amazon):
        
#         page.wait_for_timeout(3000)
#         page.locator("//span[text()='Hello, sign in']").click()
#         page.wait_for_timeout(3000)
#         expect(page.get_by_text("Enter mobile number or email")).to_be_visible()
#         page.locator('#ap_email_login').fill("aswiniprakashan999@gmail.com")
#         page.get_by_role("button",name="Continue").click()
#         expect(page.get_by_label('Password')).to_be_visible()
#         page.locator('#ap_password').fill("Aswini@23")
#         page.locator('#signInSubmit').click()
#         page.wait_for_timeout(3000)
#         error_text = page.locator(".a-alert-content").first.inner_text().strip()
#         print(error_text)
#         assert error_text == "Your password is incorrect"
