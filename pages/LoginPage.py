from playwright.sync_api import expect
class Loginpage:
    def __init__(self,page):
        self.emailPlaceholder =  page.get_by_text("Enter mobile number or email")
        self.emailtxtBox = page.locator('#ap_email_login')
        self.continuebtn = page.get_by_role("button",name="Continue")
        self.passwordtxtBox = page.locator('#ap_password')
        self.signinbtn = page.locator('#signInSubmit')



    def validateVisibilityOfEmailTxtBox(self):
        expect(self.emailPlaceholder).to_be_visible()
    
    def login(self,email,password):
        self.emailtxtBox.fill(email)
        self.continuebtn.click()
        self.passwordtxtBox.fill(password)
        self.signinbtn.click()


