from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.email = page.get_by_test_id(f'{identifier}-email-input').locator('input')
        self.username = page.get_by_test_id(f'{identifier}-username-input').locator('input')
        self.password = page.get_by_test_id(f'{identifier}-password-input').locator('input')

    def fill_registration_form(self, email: str, password: str, username: str):
        self.email.fill(email)
        expect(self.email).to_have_value(email)
        self.username.fill(username)
        expect(self.username).to_have_value(username)
        self.password.fill(password)
        expect(self.password).to_have_value(password)

    def check_visible(self):
        expect(self.email).to_be_visible()
        expect(self.email).to_have_text('user@gmail.com')
        expect(self.username).to_be_visible()
        expect(self.username).to_have_text('username')
        expect(self.password).to_be_visible()
        expect(self.password).to_have_text('password')
