from pages.form_page import FormPage
from playwright.sync_api import sync_playwright

class InputForm:  
    def __init__(self):
        # Initialize the class with a placeholder for the page object.
        # This will later be replaced with an actual Playwright page instance.
        self.page = ""

    def run_input_forms_process(self):
        # Start a Playwright automation session
        with sync_playwright() as p:
            # Launch the Edge browser (channel="msedge").
            # headless=False → browser window is visible.
            # slow_mo=50 → adds a small delay between actions for easier debugging.
            browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=50)

            # Create a new browser page (tab) instance.
            page = browser.new_page()

            # Bind the page to your FormPage class for modular automation.
            form_page = FormPage(page)

            print("process running")

            # Step 1: Open the RPA Challenge website.
            form_page.open_website("https://rpachallenge.com/")

            # Step 2: Download the report (custom method in FormPage).
            form_page.download_report()

            # Step 3: Read Excel data and map it to form fields.
            # This will loop through rows and fill the form automatically.
            form_page.read_and_map_excel()

            print("process completed")

            # Pause execution so you can interact with the browser manually
            # (useful for debugging or inspecting the filled form).
            page.close()