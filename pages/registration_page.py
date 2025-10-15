from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page, identifier='registration-form')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
