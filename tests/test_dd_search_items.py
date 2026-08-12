from playwright.sync_api import expect,Page
import pytest
from pages.HomePage import Homepage
from pages.ResultPage import ResultPage
from utils.serachitemsJsonutil import searchiteamjson_load
#serach_items = ['laptop','smartphone','pen','bag','xyzabc1235']

serach_items = searchiteamjson_load()
@pytest.mark.validsearchitem
@pytest.mark.parametrize("item",serach_items)
def test_search_items(item,page:Page,navigate_to_amazon):
    homePageobj = Homepage(page)
    resultPageobj = ResultPage(page)

    homePageobj.enterSearchProduct(item)
    homePageobj.clickOnSearch()
    page.wait_for_timeout(3000)
    expect(resultPageobj.resulttxt).to_be_visible()
    print(item,"is avaliable")

@pytest.mark.invalidsearchitem
def test_invalidIteamSearchResult(page:Page,navigate_to_amazon):
    page.locator('input#twotabsearchtextbox').fill("xyzabc12345")
    page.locator('input#nav-search-submit-button').click()
    msg = page.locator('//span[text()="No results for your search query. "]').text_content()
    print("\n",msg)
    expect(page.locator('//span[text()="No results for your search query. "]')).to_be_visible()
    page.wait_for_timeout(3000)
    
