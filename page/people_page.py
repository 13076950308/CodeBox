from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PeoplePage(BaseAction):
    add_new_contact_button = By.ID, "com.android.contacts:id/floating_action_button"

    # 点击添加新联系人按钮
    def click_add_contact(self):
        self.base_click_element(self.add_new_contact_button)
