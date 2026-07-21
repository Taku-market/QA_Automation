from playwright.sync_api import Page

def test_page_title(page: Page):
    page.goto("https://example.com")
    assert "Example" in page.title()

def test_page_has_heading(page: Page):
    page.goto("https://example.com")
    heading = page.locator("h1")
    assert heading.is_visible()

def test_search_on_google(page: Page):
    page.goto("https://www.google.com")
    page.locator('textarea[name="q"]').fill("pytest")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    assert "pytest" in page.title()

def test_wikipedia_search(page: Page):
    page.goto("https://www.wikipedia.org")
    page.locator('input[name="search"]').fill("Python programming")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    assert "Python" in page.title()