class FormPage:
    def __init__(self, page):
        self.page = page
        self.download_btn = page.get_by_role("link", name="Download Excel cloud_download")

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
            download.save_as("C:\\Users\\khang\\Finance_InvoiceProcessing_Automation\\data\\" + download.suggested_filename)
            print("report downloaded")
        else:
            print("Download button not found.")