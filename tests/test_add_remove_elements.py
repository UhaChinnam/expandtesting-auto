import os
from playwright.sync_api import Page, expect

def test_add_remove_elements(page: Page):
    """Test dynamically adding and removing an element."""
    page.goto("https://practice.expandtesting.com/add-remove-elements")
    
    # Click Add Element button twice
    add_btn = page.get_by_role("button", name="Add Element")
    add_btn.click()
    add_btn.click()
    
    # Verify two Delete buttons appeared
    delete_btns = page.get_by_role("button", name="Delete")
    expect(delete_btns).to_have_count(2)
    
    # Click the first Delete button
    delete_btns.first.click()
    
    # Verify only one Delete button remains
    expect(delete_btns).to_have_count(1)
    
    os.makedirs("reports/screenshots", exist_ok=True)
    page.screenshot(path="reports/screenshots/add_remove_elements.png")
