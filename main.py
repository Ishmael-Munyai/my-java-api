from models.form import FormPage
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
    browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=50)
    page = browser.new_page()

    form_page = FormPage(page)

    print("bot has started")
    form_page.open("https://rpachallenge.com/")

    form_page.page.wait_for_load_state('networkidle')

    form_page.download_report()
    form_page.page.pause()