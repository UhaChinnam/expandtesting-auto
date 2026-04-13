import os
from playwright.sync_api import Page, expect

def test_drag_and_drop(page: Page):
    """Test drag and drop between two columns."""
    page.goto("https://practice.expandtesting.com/drag-and-drop")
    
    col_a = page.locator("#column-a")
    col_b = page.locator("#column-b")
    
    # Verify initial state
    expect(col_a).to_have_text("A")
    expect(col_b).to_have_text("B")
    
    # Perform drag and drop
    col_a.drag_to(col_b)
    
    # Verify swapped state
    expect(col_a).to_have_text("B")
    expect(col_b).to_have_text("A")
    
    os.makedirs("reports/screenshots", exist_ok=True)
    page.screenshot(path="reports/screenshots/drag_and_drop.png")
