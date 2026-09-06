from org.sikuli.script import ImagePath, Pattern
import os
import sys
# Add necessary POI jars to the path
sys.path.append("C:\Users\khang\OneDrive\Documents\poi-3.11.jar")
sys.path.append("C:\Users\khang\OneDrive\Documents\poi-ooxml-full-5.0.0.jar")


class FormPage:
    def __init__(self, screen):
        # Set the bundle path once (no self.)
        image_path = r"C:\\Users\\khang\\OneDrive\\Documents\\New folder (3)\\bot_test\\images"
        ImagePath.setBundlePath(image_path)
        self.screen = screen
        self.download_btn = Pattern("downloadFile_image.png").similar(0.2)
        #self.submit_btn = Pattern("submit.png").similar(0.5)

        
        
        # Patterns for fields (screenshots saved as images)
        self.fields = {
            "FirstName": Pattern("FirstName.png").similar(0.7),
            "LastName": Pattern("LastName.png").similar(0.7),
            "Email": Pattern("Email.png").similar(0.8),
            "Phone": Pattern("Phone.png").similar(0.8),
            "CompanyName":Pattern("CompanyName.png").similar(0.8),
            "Address":Pattern("Address.png").similar(0.8)
            }
            
            
    
    def download_file(self, download_dir, target_dir):
        """Click the download file button if it exists."""
        self.screen.wait(0.30)
        self.screen.highlight(0.3)
        if self.screen.exists(self.download_btn, 5):
            print("Downloading file...")
            self.screen.click(self.download_btn)

            # Wait a few seconds for the file to appear
            self.screen.wait(0.30)
            
            # Find the most recent file in the download directory
    def get_latest_excel(self, download_dir):
        while True:
            files = [f for f in os.listdir(download_dir) if f.endswith(".xlsx")]
            if files:
                latest_file = max(
                    [os.path.join(download_dir, f) for f in files],
                    key=os.path.getmtime
                )
                return latest_file
     


    """        
    def fill_field(self, field_name, value):
        if field_name in self.fields:
            pattern = self.fields[field_name]
            if self.screen.exists(pattern, 5):
                self.screen.click(pattern)
                self.screen.type(value)

    
    """

    def submit_form(self):
        if self.screen.exists(self.submit_btn, 5):
            self.screen.click(self.submit_btn)
        else:
            print("Submit button not found")
            
            
    def read_excel_rows(self,file_path):
        #Load the Excel file
        #df = pd.read_excel(file_path)

        #Iterate row by row
        #for index, row in df.iterrows():
        print("Row {index}:")
            
        #for col in df.columns:
        print("  {col}: {row[col]}")
        print("-" * 40)
