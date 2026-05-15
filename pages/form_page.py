import pandas as pd
import time
from playwright.sync_api import sync_playwright

class FormPage:
    def __init__(self, page):
        self.page = page
        self.filename = f"challenge_{int(time.time())}.xlsx"
        self.download_btn = page.get_by_role("link", name="Download Excel cloud_download")
        self.submit_btn = page.get_by_role("button", name="Submit")
        self.start_btn = page.get_by_role("button", name="Start")
        self.field_mapping = {
            "First Name": "input[ng-reflect-name='labelFirstName']",
            "Last Name ": "input[ng-reflect-name='labelLastName']",
            "Company Name": "input[ng-reflect-name='labelCompanyName']",
            "Role in Company": "input[ng-reflect-name='labelRole']",
            "Address": "input[ng-reflect-name='labelAddress']",
            "Email": "input[ng-reflect-name='labelEmail']",
            "Phone Number": "input[ng-reflect-name='labelPhone']"
        }

    def open(self, url):
        self.page.goto(url)

    def download_report(self):
        if self.download_btn.is_visible():
            # Start waiting for the download
            with self.page.expect_download() as download_info:
                # Perform the action that initiates download
                self.download_btn.click()
            download = download_info.value

            # Wait for the download process to complete and save the downloaded file somewhere
            download.save_as(r"C:\Users\khang\Finance_InvoiceProcessing_Automation\data\\" + self.filename)
            print("report downloaded")
        else:
            print("Download button not found.")

    def read_and_map_excel(self):
        data = pd.read_excel(r"C:\Users\khang\Finance_InvoiceProcessing_Automation\data\\" + self.filename)
        print(data.columns.tolist())

        mapped_data = []

        # Wait until the Start button is visible and then click it
        self.start_btn.wait_for(state="visible")
        self.start_btn.click()

        for _, row in data.iterrows():
            for field, selector in self.field_mapping.items():
                if field in row and pd.notna(row[field]):
                    value = str(row[field])

                    # Log the action
                    print(f"Filling {selector} with {value}")
                    self.page.fill(selector, value)
                    
                

            # Wait for 3 seconds
            self.page.wait_for_timeout(3000)

            print("submitting form")
            self.submit_btn.wait_for(state="visible")
            self.submit_btn.click()
            
        return mapped_data

    def fill_form(self, data):
        """
        data: dict containing one row of Excel data
        field_mapping: dict mapping Excel column names -> CSS selectors
        """
        for field, selector in self.field_mapping.items():
            if field in data and pd.notna(data[field]):
                self.page.fill(selector, str(data[field]))
        self.page.click("button[type='submit']")
 