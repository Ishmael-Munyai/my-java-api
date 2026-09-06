from lackey import *

class SubmitPage:
    def __init__(self, screen):
        self.screen = screen
        self.submit_btn = Pattern("submit.png").similar(0.8)

    def submit_form(self):
        if self.screen.exists(self.submit_btn, 5):
            self.screen.click(self.submit_btn)
        else:
            print("Submit button not found")
