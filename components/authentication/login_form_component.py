from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.email = page.get_by_test_id(f'{identifier}-email-input').locator('input')
        self.password = page.get_by_test_id(f'{identifier}-password-input').locator('input')

    def fill_login_form(self, email: str, password: str):
        self.email.fill(email)
        expect(self.email).to_have_value(email)
        self.password.fill(password)
        expect(self.password).to_have_value(password)

    def check_visible(self):
        expect(self.email).to_be_visible()
        expect(self.password).to_be_visible()
