import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SettingPage(BaseAction):
    # 关于百年奥莱选项
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"
    # 清理缓存选项
    clear_cache_button = By.XPATH, "//*[@text='清理缓存']"
    # 地址管理 按钮
    address_list_button = By.XPATH, "//*[@text='地址管理']"

    # 点击关于百年奥莱
    @allure.step(title="设置 点击 关于百年奥莱")
    def click_about(self):
        # 调用边滑边找方法,因为百年奥莱选项在屏幕下方
        self.find_element_with_scroll(self.about_button).click()

    # 点击清理缓存
    @allure.step(title="设置 点击 清理缓存")
    def click_clear_cache(self):
        # 调用边滑边找方法,因为百年奥莱选项在屏幕下方
        self.find_element_with_scroll(self.clear_cache_button).click()

    # 点击地址管理
    @allure.step(title="设置 点击 地址管理")
    def click_address_list(self):
        # 调用边滑边找方法,因为百年奥莱选项在屏幕下方
        self.find_element_with_scroll(self.address_list_button).click()