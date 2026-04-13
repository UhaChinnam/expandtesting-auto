import os
from playwright.sync_api import Page, expect

def test_file_upload(page: Page):
    """Test file upload workflow."""
    page.goto("https://practice.expandtesting.com/upload")
    
    # Create a dummy file to upload
    with open("dummy_upload.txt", "w") as f:
        f.write("This is a test file for upload.")
        
    try:
        # Standard ID for upload input is usually fileUpload or fileSubmit
        file_input = page.locator("input[type='file']")
        file_input.set_input_files("dummy_upload.txt")
        
        # Click upload button
        page.locator("button[type='submit'], input[type='submit']").first.click()
        
        # Verify success
        expect(page.locator("#uploaded-files")).to_contain_text("dummy_upload.txt")
        
        os.makedirs("reports/screenshots", exist_ok=True)
        page.screenshot(path="reports/screenshots/file_upload.png")
    finally:
        if os.path.exists("dummy_upload.txt"):
            os.remove("dummy_upload.txt")
