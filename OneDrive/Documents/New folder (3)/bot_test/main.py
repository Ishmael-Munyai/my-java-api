from org.sikuli.script import Screen
#from org.sikuli.script import Screen
from pages.browserPage import BrowserPage
from pages.form_page import FormPage

def run():
    # Create Screen object once
    screen = Screen(0)

# Initialize BrowserPage with Screen
    browser = BrowserPage(screen)

    # Path to Edge
    exe_path = r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    url = "https://rpachallenge.com/"
    download_dir = r"C:\Users\khang\Downloads"
    
    target_dir = r"C:\Users\khang\OneDrive\Documents\New folder (3)\bot_test\Reports"
    
    # Open some application
    browser.open_browser(exe_path)
    browser.navigate(url)
    
    # Initialize FormPage
    form_page = FormPage(screen)

    # Download a report
    form_page.download_file(download_dir, target_dir)
    
    latest_excel =  form_page.get_latest_excel(download_dir)
    print("Latest Excel file:", latest_excel)
                
    form_page.read_excel_rows(latest_excel)

if __name__ == "__main__":
    run()