from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class QuickContactActivityPage(BaseAction):
    contact_name_text = By.ID, "com.android.contacts:id/large_title"
    phone_number_text = By.ID, "com.android.contacts:id/header"

    # 获取联系人的姓名
    def get_contact_name(self):
        return self.base_get_content(self.contact_name_text)

    # 获取联系的电话
    def get_contact_phone(self):
        return self.base_get_content(self.phone_number_text)
