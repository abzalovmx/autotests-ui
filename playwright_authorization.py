from playwright.sync_api import expect, sync_playwright
# 14-08

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=10)
#     page = browser.new_page()
#
#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#
#     email_input = page.get_by_test_id('login-form-email-input').locator('input')
#     email_input.fill('as@s.rz')
#
#     password_input = page.get_by_test_id('login-form-password-input').locator('input')
#     password_input.fill('PASSWORD')
#
#     login_button = page.get_by_test_id('login-page-login-button')
#     login_button.click()
#
#     wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
#     expect(wrong_email_or_password_alert).to_be_visible()
#     expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
#
#     page.wait_for_timeout(2000)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill('username')

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()