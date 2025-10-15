from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.create_course_title = page.get_by_test_id(f'{identifier}-title-text')
        self.create_course_button = page.get_by_test_id(f'{identifier}-create-course-button')

    def check_visible(self, is_create_course_disabled=True):
        expect(self.create_course_title).to_have_text('Create course')
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()

        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        expect(self.create_course_button).to_be_visible()
        self.create_course_button.click()
