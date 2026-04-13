import os
from playwright.sync_api import Page, expect

def test_dynamic_controls_ui_assertions(page: Page):
    """Test UI assertions using Playwright's auto-retrying expectations."""
    page.goto("https://practice.expandtesting.com/dynamic-controls")
    
    # ASSERTION 1: Verify checkbox state and visibility
    checkbox_container = page.locator("#checkbox")
    checkbox_input = page.locator("#checkbox input")
    expect(checkbox_container).to_be_visible()
    expect(checkbox_input).not_to_be_checked()
    
    # Interact with the Remove button and assert UI changes
    remove_btn = page.get_by_role("button", name="Remove")
    remove_btn.click()
    
    # Assert loading text appears then disappears
    expect(page.locator("#loading")).to_have_text("Wait for it... ")
    
    # Assert checkbox is gone
    expect(checkbox_container).to_be_hidden()
    
    # Assert success message
    expect(page.locator("#message")).to_have_text("It's gone!")
    
    # Assert the button changed to "Add"
    add_btn = page.get_by_role("button", name="Add")
    expect(add_btn).to_be_visible()
    
    # ASSERTION 2: Verify Enable/Disable input field
    input_field = page.locator("#input-example input")
    expect(input_field).to_be_disabled()
    
    # Click enable
    enable_btn = page.get_by_role("button", name="Enable")
    enable_btn.click()
    
    # Assert loading state
    expect(page.locator("#input-example #loading")).to_be_visible()
    
    # Assert input becomes enabled and success message appears
    expect(input_field).to_be_enabled()
    expect(page.locator("#message")).to_have_text("It's enabled!")
    
    # Type into the enabled field (UI interaction assertion)
    input_field.fill("Hello Automation")
    expect(input_field).to_have_value("Hello Automation")
    
    # Save screenshot proof
    os.makedirs("reports/screenshots", exist_ok=True)
    page.screenshot(path="reports/screenshots/dynamic_controls_ui.png")
