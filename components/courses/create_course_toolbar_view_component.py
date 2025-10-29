from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
import allure


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.create_course_title = Text(page, f'{identifier}-title-text', 'Title')
        self.create_course_button = Button(page, f'{identifier}-create-course-button', 'Button')

    @allure.step('Check visible course toolbar')
    def check_visible(self, is_create_course_disabled=True):
        self.create_course_title.check_have_text('Create course')
        if is_create_course_disabled:
            self.create_course_title.check_visible()

        else:
            self.create_course_button.check_disabled()

    def click_create_course_button(self):
        self.create_course_button.check_visible()
        self.create_course_button.click()
