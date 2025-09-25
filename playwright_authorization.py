from playwright.sync_api import expect, sync_playwright
# 14-08

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False, slow_mo=600)
    page = chromium.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
