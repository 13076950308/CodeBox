import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AboutPage(BaseAction):
    # 版本更新按钮
    update_button = By.XPATH, "//*[@text='版本更新']"

    # 点击版本更新按钮
    @allure.step(title="关于百年奥莱 点击 更新版本")
    def click_update(self):
        # 不需要调用边滑边找方法,因为版本更新按钮不能动
        self.base_click_element(self.update_button)