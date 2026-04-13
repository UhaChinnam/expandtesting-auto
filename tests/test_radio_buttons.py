import os
from playwright.sync_api import Page, expect

def test_radio_buttons(page: Page):
    """Test radio buttons selection and functionality."""
    page.goto("https://practice.expandtesting.com/radio-buttons")
    
    # We try to select a typical color radio like Blue or Red
    # Expandtesting usually has color radio buttons
    blue_radio = page.locator('input[type="radio"][id="blue"]')
    red_radio = page.locator('input[type="radio"][id="red"]')
    
    # Check "Blue"
    if blue_radio.count() == 0:
        # Fallback to get_by_role if ID is different
        blue_radio = page.get_by_role("radio", name="Blue")
        red_radio = page.get_by_role("radio", name="Red")

    blue_radio.check()
    expect(blue_radio).to_be_checked()
    
    # Check another and verify the first is unchecked
    red_radio.check()
    expect(red_radio).to_be_checked()
    expect(blue_radio).not_to_be_checked()
    
    os.makedirs("reports/screenshots", exist_ok=True)
    page.screenshot(path="reports/screenshots/radio_buttons.png")
