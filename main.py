from models.search import SearchPage
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
    browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=50)
    page = browser.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")