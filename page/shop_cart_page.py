import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class ShopCartPage(BaseAction):
    # 全选按钮
    select_all_button = By.ID, "com.yunmall.lc:id/iv_select_all"
    # 编辑按钮
    edit_button = By.XPATH, "//*[@text='编辑']"
    # 删除按钮
    delete_button = By.XPATH, "//*[@text='删除']"
    # 确认按钮
    affirm_button = By.XPATH, "//*[@text='确认']"
    # 完成按钮
    accomplish_button = By.XPATH, "//*[@text='完成']"
    # 加号按钮
    add_button = By.ID, "com.yunmall.lc:id/iv_add"
    # 单价特征
    price_feature = By.ID, "com.yunmall.lc:id/tv_price"
    # 总价特征
    total_price_feature = By.ID, "com.yunmall.lc:id/tv_count_money"

    # 点击全选
    @allure.step(title="购物车 点击 全选")
    def click_select_all(self):
        self.base_click_element(self.select_all_button)

    # 点击编辑
    @allure.step(title="购物车 点击 编辑")
    def click_edit(self):
        self.base_click_element(self.edit_button)

    # 点击删除
    @allure.step(title="购物车 点击 删除")
    def click_delete(self):
        self.base_click_element(self.delete_button)

    # 点击确认
    @allure.step(title="购物车 点击 确认")
    def click_affirm(self):
        self.base_click_element(self.affirm_button)

    # 点击完成
    @allure.step(title="购物车 点击 完成")
    def click_accomplish(self):
        self.base_click_element(self.accomplish_button)

    # 点击加号
    @allure.step(title="购物车 点击 加号")
    def click_add(self):
        self.base_click_element(self.add_button)

    # 获取单价
    @allure.step(title="购物车 点击 获取单价")
    def get_price(self):
        # 获取单价的文字
        price_text = self.base_get_content(self.price_feature)
        # 通过deal_with_price(price_text)去掉前面的人民币符号，并且转换成float类型
        return self.deal_with_price(price_text)

    # 获取总价
    @allure.step(title="购物车 点击 获取总价")
    def get_total_price(self):
        # 获取单价的文字
        price_text = self.base_get_content(self.total_price_feature)
        # 通过deal_with_price(price_text)去掉前面的人民币符号，并且转换成float类型
        return self.deal_with_price(price_text)

    # 处理价格
    def deal_with_price(self, price):
        return float(price[2:])

    # 判断购物车是否为空
    @allure.step(title="购物车 判断 购物车是否为空")
    def is_shop_cart_empty(self):
        xpath = By.XPATH, "//*[contains(@text, '购物车还是空的')]"
        return self.base_is_feature_exist(xpath)
