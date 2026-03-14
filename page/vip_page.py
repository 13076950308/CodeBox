import allure
import time

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class VipPage(BaseAction):
    # 邀请码输入框
    invete_edit_text = By.XPATH, "//input[@type='tel']"
    # 立即成为会员 按钮
    be_vip_button = By.XPATH, "//input[@value='立即成为会员']"

    # 输入邀请码
    @allure.step(title="vip页面 输入 邀请码")
    def input_invite(self, text):
        self.base_input_content(self.invete_edit_text, text)

    # 点击立即成为会员
    @allure.step(title="vip页面 点击 成为会员")
    def click_be_vip(self, text):
        self.base_click_element(self.be_vip_button)
        time.sleep(2)  # Web环境出来需要时间
