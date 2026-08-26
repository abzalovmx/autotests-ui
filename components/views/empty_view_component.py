from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

    def check_visible(self, title: str, description: str):
        expect(self.icon).to.be_visible()
        expect(self.title).to.be_visible()
        expect(self.title).to_have_text(title)
        expect(self.description).to.be_visible()
        expect(self.description).to_have_text(description)
