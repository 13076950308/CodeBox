from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):
    # 我 按钮
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 点击我
    def click_me(self):
        self.base_click_element(self.me_button)
