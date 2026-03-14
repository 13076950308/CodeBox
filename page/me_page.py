import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class MePage(BaseAction):
    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    # 设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 加入超级VIP
    be_vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    # 点击姓名输入框
    @allure.step(title="我 获取 昵称")
    def get_nick_name_text(self):
        return self.base_get_content(self.nick_name_text_view)

    # 点击设置按钮
    @allure.step(title="我 点击 设置")
    def click_setting(self):
        self.find_element_with_scroll(self.be_vip_button).click()

    # 点击“加入超级VIP”选项
    @allure.step(title="我 点击 加入vip")
    def click_be_vip(self):
        self.find_element_with_scroll(self.be_vip_button).click()