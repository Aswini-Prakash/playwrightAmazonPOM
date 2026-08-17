import allure
from playwright.sync_api import sync_playwright,expect,Page
import pytest
#Page ,Context, these are the type in playwright

from pages.HomePage import Homepage
from pages.LoginPage import Loginpage
from pages.ResultPage import ResultPage
from pages.ShoppingCartPage import ShoppingCartPage
@pytest.mark.visibility

def test_validatePageComponents(page:Page,navigate_to_amazon):
        print("\nURL :", page.url)
        page.wait_for_timeout(5000)
        print("Before Title :", repr(page.title()))
        expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        print("After Title :", repr(page.title()))
        expect(page).to_have_url("https://www.amazon.in/")
        page.wait_for_timeout(2000)
@pytest.mark.visibility

def test_validateHeaders(page:Page,navigate_to_amazon):
        expect(page.locator('input#twotabsearchtextbox')).to_be_visible()
        expect(page.locator('input#twotabsearchtextbox')).to_be_enabled()
@pytest.mark.visibility

def test_validateLogoAndSearch(page:Page,navigate_to_amazon):
        expect(page.locator('#nav-logo-sprites')).to_be_visible()
        expect(page.get_by_placeholder("Search Amazon.in")).to_be_visible()
@pytest.mark.visibility

def test_validateVisibilityOnCarticonReturnsAndOrdersSigin(page:Page,navigate_to_amazon):
        shoppingCartPageObj = ShoppingCartPage(page)
        homepageObj = Homepage(page)
        expect(shoppingCartPageObj.cartIcon).to_be_visible()
        expect(homepageObj.retursAndOrederLink).to_be_visible()
        expect(homepageObj.loginbtn).to_be_visible()

        




