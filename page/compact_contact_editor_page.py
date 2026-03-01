from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class CompactContactEditorPage(BaseAction):
    name_input_box = By.XPATH, "//*[@text='姓氏']"
    telephone_input_box = By.XPATH, "//*[@text='电话']"
    save_button = By.XPATH, "//*[@text='保存']"

    # 点击姓名输入框
    def click_name_input_box(self):
        self.base_click_element(self.name_input_box)

    # 输入姓名
    def input_name_input_box(self, name):
        self.base_input_content(self.name_input_box, name)

    # 点击电话输入框
    def click_telephone_input_box(self):
        self.base_click_element(self.telephone_input_box)

    # 输入电话号码
    def input_telephone_input_box(self, telephone_number):
        self.base_input_content(self.telephone_input_box, telephone_number)

    # 点击保存按钮
    def click_save_button(self):
        self.base_click_element(self.save_button)
