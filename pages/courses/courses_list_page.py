from components.courses.courses_list_toolbar_view import CoursesListToolbarViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
from playwright.sync_api import Page
from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page, identifier='courses-list')
        self.course_view = CourseViewComponent(page)
        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.toolbar_view = CoursesListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
