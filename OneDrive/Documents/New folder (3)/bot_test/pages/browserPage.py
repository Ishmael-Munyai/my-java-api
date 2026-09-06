from org.sikuli.script import Key

class BrowserPage:
    def __init__(self, screen):
        # Set the bundle path once (no self.)
        #ImagePath.setBundlePath(r"C:\\Users\\khang\\OneDrive\\Documents\\New folder (3)\\bot_test\\images")
        self.screen = screen

    def open_browser(self, exe_path):
        """Open the browser using its executable path."""
        self.screen.type("r", Key.WIN)
        self.screen.type(exe_path)
        self.screen.type(Key.ENTER)
        self.screen.wait(0.3)
        print("Browser is open")

    def navigate(self, url):
        """Navigate to a given URL after browser opens."""
        # Focus the address bar
        self.screen.wait(0.5)
        self.screen.type("l", Key.CTRL)
        self.screen.type(url)
        self.screen.type(Key.ENTER)
