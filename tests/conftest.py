import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


# Фикстура без использования pytest-playwright встроенной фикстуры
# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#
#         yield context.new_page()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)

    yield browser.new_page()
    browser.close()
