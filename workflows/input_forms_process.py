from pages.form_page import FormPage
from playwright.sync_api import sync_playwright

class InputForm:
    def __init__(self):
        self.page = ""

    def run_input_forms_process(self):
        with sync_playwright() as p:
            # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
            browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=50)

            # Create a new browser page instance and bind it to FormPage for automation
            page = browser.new_page()

            form_page = FormPage(page)

            print("process running")


            # Open the RPA Challenge website in the browser
            form_page.open("https://rpachallenge.com/")
        

            ## Trigger the download of the challenge report from the web page
            form_page.download_report()

            # Read Excel file and map each row into structured form input data
            input_forms = form_page.read_and_map_excel()

            # Iterate through each mapped form entry from Excel and print its contents for debugging
            for form in input_forms:
                print(form)

            print("process completed")

            page.pause()