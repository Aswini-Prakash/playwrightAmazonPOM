from playwright.sync_api import sync_playwright,expect,Page
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

