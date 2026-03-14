import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址按钮
    add_address_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"
    # 默认的姓名和电话的特征
    default_receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"
    # 默认标记
    default_flag = By.ID, "com.yunmall.lc:id/address_is_default"
    # 编辑按钮
    edit_button = By.XPATH, "//*[@text='编辑']"
    # 删除按钮
    delete_button = By.XPATH, "//*[@text='删除']"
    # 确定按钮
    confirm_button = By.XPATH, "//*[@text='确认']"

    # 点新增地址
    @allure.step(title="地址列表 点击 添加地址")
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()

    # 获取默认地址的电话和文字信息
    @allure.step(title="地址列表 获取 收件人和电话的标题")
    def get_default_receipt_name_text(self):
        return self.base_get_content(self.default_receipt_name_text_view)

    # 判断默认标记是否存在
    @allure.step(title="判断默认标记是否存在")
    def is_default_feature_exist(self):
        return self.base_is_feature_exist(self.default_flag)

    # 判断删除按钮是否存在
    @allure.step(title="判断删除按钮是否存在")
    def is_delete_feature_exist(self):
        return self.base_is_feature_exist(self.delete_button)

    # 点击默认地址
    @allure.step(title="地址列表 点击 默认地址")
    def click_default_address(self):
        self.base_click_element(self.default_flag)

    # 点击编辑
    @allure.step(title="地址列表 点击 编辑")
    def click_edit(self):
        self.base_click_element(self.edit_button)

    # 点击删除
    @allure.step(title="地址列表 点击 删除")
    def click_delete(self):
        self.base_click_element(self.delete_button)

    # 点击确定
    @allure.step(title="地址列表 点击 确定")
    def click_confirm(self):
        self.base_click_element(self.confirm_button)
