from pages.form_page import FormPage
from playwright.sync_api import sync_playwright
from workflows.input_forms_process import InputForm

def execute():
    input_form = InputForm()

    #Filling out online input forms
    input_form.run_input_forms_process()

if __name__ == "__main__":
    execute()