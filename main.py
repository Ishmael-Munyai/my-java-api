import schedule
import time
from pages.form_page import FormPage
from playwright.sync_api import sync_playwright
from workflows.input_forms_process import InputForm

def execute():
    input_form = InputForm()

    #Filling out online input forms
    input_form.run_input_forms_process()

if __name__ == "__main__":
    # Schedule to run every 3 minutes
    schedule.every(3).minutes.do(execute)

    # Keep the scheduler alive
    while True:
        schedule.run_pending()
        time.sleep(1)