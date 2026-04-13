from playwright.sync_api import Page, expect

def test_form_inputs(page: Page):
    """Test standard form input validations."""
    page.goto("https://practice.expandtesting.com/inputs")
    
    # Number input
    number_input = page.locator("#input-number")
    number_input.fill("12345")
    expect(number_input).to_have_value("12345")
    
    # Text input
    text_input = page.locator("#input-text")
    text_input.fill("Hello World")
    expect(text_input).to_have_value("Hello World")
    
    # Password input
    password_input = page.locator("#input-password")
    password_input.fill("Secret123!")
    expect(password_input).to_have_value("Secret123!")
    # Verify type is password
    expect(password_input).to_have_attribute("type", "password")
    
    # Date input
    date_input = page.locator("#input-date")
    date_input.fill("2025-01-01")
    expect(date_input).to_have_value("2025-01-01")
    
    # Click display inputs to trigger output rendering
    page.locator("#btn-display-inputs").click()
    
    # Validate the resulting outputs
    expect(page.locator("#output-number")).to_have_text("12345")
    expect(page.locator("#output-text")).to_have_text("Hello World")
    expect(page.locator("#output-password")).to_have_text("Secret123!")
    expect(page.locator("#output-date")).to_have_text("2025-01-01")
