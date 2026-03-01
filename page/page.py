from page.people_page import PeoplePage
from page.quick_contact_activity_page import QuickContactActivityPage
from page.compact_contact_editor_page import CompactContactEditorPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def people_activity(self):
        return PeoplePage(self.driver)

    @property
    def compact_contact_editor_activity(self):
        return CompactContactEditorPage(self.driver)

    @property
    def quick_contact_activity(self):
        return QuickContactActivityPage(self.driver)
