import pytest
from playwright.sync_api import Page, expect

def test_broken_images(page: Page):
    """Test for broken images by verifying naturalWidth."""
    page.goto("https://practice.expandtesting.com/broken-images")
    
    # Get all images within the container
    images = page.locator(".container img").all()
    
    broken_count = 0
    valid_count = 0
    
    for img in images:
        # Check if the image has a natural rendering width
        # If naturalWidth is 0, the image is broken
        is_broken = page.evaluate("img => img.naturalWidth === 0", img.element_handle())
        if is_broken:
            broken_count += 1
        else:
            valid_count += 1
            
    # Based on the website's known state, there are typically 2 broken images and 1 valid image
    # We assert that we can detect broken images
    assert broken_count > 0, "No broken images detected when there should be some."
    assert valid_count > 0, "No valid images detected when there should be at least one."

def test_broken_links_network(page: Page):
    """Test broken links via analyzing HTTP responses."""
    broken_urls = []
    
    # Listen to response events
    page.on("response", lambda response: broken_urls.append(response.url) if response.status >= 400 else None)
    
    # Navigate to status codes page which has 404, 500 etc. links
    page.goto("https://practice.expandtesting.com/status-codes")
    
    # Click the 404 link explicitly
    with page.expect_response(lambda response: "404" in response.url and response.status == 404):
        page.get_by_role("link", name="404").click()
        
    assert len(broken_urls) > 0, "Failed to capture broken link responses"
