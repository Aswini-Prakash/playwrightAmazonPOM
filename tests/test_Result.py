from playwright.sync_api import sync_playwright,expect,Page
import pytest

from pages.HomePage import Homepage
from pages.LoginPage import Loginpage
from pages.ResultPage import ResultPage
from utils.productutil import read_product
def test_validateTheResultTitle(page:Page,navigate_to_amazon):
    page.locator('input#twotabsearchtextbox').fill("iphone")
    page.locator('input#nav-search-submit-button').click()
    page.locator("//h2[text()='Results']").wait_for(state="visible")
    expect(page).to_have_title("Amazon.in : iphone")

def test_invalidIteamSearchResult(page:Page,navigate_to_amazon):
    page.locator('input#twotabsearchtextbox').fill("xyzabc12345")
    page.locator('input#nav-search-submit-button').click()
    msg = page.locator('//span[text()="No results for your search query. "]')
    print("\n",msg)
    expect(page.locator('//span[text()="No results for your search query. "]')).to_be_visible()

@pytest.mark.searchitem
def test_searchProduct(page:Page,navigate_to_amazon):
        homepageObj= Homepage(page)
        resultPageObj= ResultPage(page)
        homepageObj.enterSearchProduct("bulb")
        homepageObj.clickOnSearch()
        #expect(page.get_by_text("Results")).to_be_visible()
        page.wait_for_timeout(3000)
        print("\n page title ->",page.title())
        expect(page).to_have_title("Amazon.in : bulb")
        before_count= resultPageObj.validateCartCount()
        page.wait_for_timeout(3000)
        print("\n",before_count)
        product = read_product()
        print(product)
        resultPageObj.clickOnAddToCartbtn(product)
        page.wait_for_timeout(3000)
        after_count = resultPageObj.validateCartCount()
        print("\n",after_count)
        assert after_count == before_count +1
        print("CartCount passed")

