import re
from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    """Test successful login validation."""
    page.goto("https://practice.expandtesting.com/login")
    
    # Fill in the standard practice credentials
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    
    # Verify successful login via flash message and URL
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page).to_have_url(re.compile(r".*/secure$"))

def test_login_failure(page: Page):
    """Test invalid login validation."""
    page.goto("https://practice.expandtesting.com/login")
    
    # Fill in invalid credentials
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()
    
    # Verify failure via flash message
    expect(page.locator("#flash")).to_contain_text("Your password is invalid!")
