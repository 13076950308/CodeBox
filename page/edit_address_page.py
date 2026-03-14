import allure
import random
import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    # 收件人输入框
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    # 手机号输入框
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    # 详细地址输入框
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    # 邮编输入框
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    # 设为默认地址按钮
    default_address_button =By.ID, "com.yunmall.lc:id/address_default"
    # 所在地区按钮
    region_button = By.ID, "com.yunmall.lc:id/address_province"
    # 省市区的元素
    area_title = By.ID, "com.yunmall.lc:id/area_title"
    # 保存按钮
    save_button = By.ID, "com.yunmall.lc:id/button_send"

    # 输入收件人
    @allure.step(title="编辑地址 输入 收件人")
    def input_name(self, text):
        self.base_input_content(self.name_edit_text, text)

    # 输入手机号
    @allure.step(title="编辑地址 输入 手机号")
    def input_phone(self, text):
        self.base_input_content(self.phone_edit_text, text)

    # 输入详细地址
    @allure.step(title="编辑地址 输入 详细地址")
    def input_info(self, text):
        self.base_input_content(self.info_edit_text, text)

    # 输入邮编
    @allure.step(title="编辑地址 输入 邮编")
    def input_post_code(self, text):
        self.base_input_content(self.post_code_edit_text, text)

    # 点击设为默认地址
    @allure.step(title="编辑地址 点击 默认地址")
    def click_default_address(self):
        self.base_click_element(self.default_address_button).click()

    # 点击所在地区
    @allure.step(title="编辑地址 点击 所在地区")
    def click_region(self):
        self.base_click_element(self.region_button)

    # 进入所在地区，并且选择一个随机的省份
    @allure.step(title="选择区域")
    def choose_region(self):
        self.click_region()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 所有的可选的省市区
            areas = self.base_find_elements(self.area_title)
            # 所有的可选的个数
            areas_count = len(areas)
            # 随机数下标
            area_index = random.randint(0, areas_count-1)
            # 获取随机的省份
            areas[area_index].click()
            time.sleep(1)

    # 点击保存
    def click_save(self):
        self.base_click_element(self.save_button)

