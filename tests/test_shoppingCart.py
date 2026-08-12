from playwright.sync_api import sync_playwright,expect,Page
import pytest

from pages.ShoppingCartPage import ShoppingCartPage
from pages.HomePage import Homepage
from pages.ResultPage import ResultPage
from utils.productutil import json_load

@pytest.mark.validatecart
def test_valiadteCartItems(page: Page, navigate_to_amazon):
    homepageObj = Homepage(page)
    resultpageObj = ResultPage(page)
    shoppingcartpageObj = ShoppingCartPage(page)

    homepageObj.enterSearchProduct("bulb")
    homepageObj.clickOnSearch()

    product = json_load("testdata/products.json")
    print("Product:", product)

    resultpageObj.clickOnAddToCartbtn(product)

    shoppingcartpageObj.clickOnCartIcon()

    page.wait_for_timeout(3000)

    shoppingcartpageObj.clickOnIncrementCartIcon()

    page.wait_for_timeout(3000)

    cart_count = resultpageObj.validateCartCount()
    print("Cart count:", cart_count)

    subitems_msg = shoppingcartpageObj.validateSubItemsMsg()
    print("Subtotal message:", subitems_msg)

    page.wait_for_timeout(3000)




    