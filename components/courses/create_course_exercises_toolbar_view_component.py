from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.exercises_title = Text(page, f'{identifier}-title-text', 'Title')
        self.create_exercise_button = Button(page, f'{identifier}-create-exercise-button', 'Button')

    def check_visible(self):
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
