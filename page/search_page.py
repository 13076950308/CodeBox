import time

import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class SearchPage(BaseAction):
    # 搜索框
    search_keyword_text = By.ID, "com.yunmall.lc:id/text_search_keyword"
    # 搜索按钮
    search_button = By.ID, "com.yunmall.lc:id/button_search"
    # 搜索搜索记录按钮
    search_del_button = By.ID, "com.yunmall.lc:id/search_del"

    # 输入文本内容
    @allure.step(title="搜索页面 输入 关键字")
    def input_keywords(self, text):
        self.base_input_content(self.search_keyword_text, text)

    # 点击搜索
    @allure.step(title="搜索页 点击 搜索按钮")
    def click_search(self):
        self.base_click_element(self.search_button)
        time.sleep(2)

    # 点击 搜索记录的删除
    @allure.step(title="搜索页 点击 删除搜索记录")
    def click_del_search(self):
        self.base_click_element(self.search_del_button)
        time.sleep(2)

    # 判断某个元素的特征是否存在
    @allure.step(title="搜索页 判断 搜索的内容是否存在")
    def is_keywords_exist(self, keyword):
        # xpath = By.XPATH, "//*[@text='%s']" % keyword
        xpath = By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % keyword
        return self.base_is_feature_exist(xpath)
        # 判断某个元素的特征是否存在

    @allure.step(title="搜索页 判断 暂无搜索历史")
    def is_search_record_empty(self, keyword):
        feature = By.XPATH, "//*[@text='暂无搜索历史']"
        return self.base_is_feature_exist(feature)