from playwright.sync_api import sync_playwright,expect,Page
import pytest

from pages.AddtocartPage import AddtocartPage
from pages.HomePage import Homepage
from pages.ResultPage import ResultPage


@pytest.mark.addtocart
def test_add_to_cart_book(page:Page,navigate_to_amazon):
        homepageObj= Homepage(page)
        resultPageObj= ResultPage(page)

        homepageObj.enterSearchProduct("book")
        homepageObj.clickOnSearch()
        #expect(page.get_by_text("Results")).to_be_visible()
        page.wait_for_timeout(3000)
        print("\n page title ->",page.title())
        expect(page).to_have_title("Amazon.in : book")

        product_page = resultPageObj.open_product_page()
        
        addtocartPageObj = AddtocartPage(product_page)
        
        addtocartPageObj.clickOnAddToCartBtn()
        page.wait_for_timeout(3000)
        


