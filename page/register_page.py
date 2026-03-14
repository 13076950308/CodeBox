import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class RegisterPage(BaseAction):
    # 已有账号去登录，按钮
    login_button = By.XPATH, "//*[@text='已有账号，去登录']"

    # 点击姓名输入框
    @allure.step(title="注册 点击 登录页面")
    def click_login(self):
        self.base_click_element(self.login_button)


