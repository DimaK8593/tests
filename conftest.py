import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(playwright_context):
    page = playwright_context.new_page()
    page.goto("https://app.todoist.com/auth/login")
    page.fill("input[type='email']", "dima2102kud@gmail.com")
    page.fill("input[type='password']", "CreatingPassword")
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")
    yield page