import time
from base.base_analyze import analyze_yaml_file
from base.base_driver import init_driver
from page.page import Page
from time import sleep
import pytest


class TestSearch:

    def setup(self):
        self.driver = init_driver(noRest=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_yaml_file('search_data.yaml', 'test_search'))
    def test_search(self, args):
        keyword = args["keyword"]
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我-点击首页
        self.page.home.click_home()
        # 首页-点击放大镜
        self.page.home.click_search()
        # 搜索-输入文字
        self.page.search.input_keywords(keyword)
        # 搜索-点击搜索按钮
        self.page.search.click_search()
        # 搜索-返回
        self.page.search.base_press_back()
        # 断言搜索的关键字，是不是存在搜索的页面
        assert self.page.search.is_keywords_exist(keyword)

    def test_del_search(self):
        # 添加删除记录
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我-点击首页
        self.page.home.click_home()
        # 首页-点击放大镜
        self.page.home.click_search()
        # 搜索-输入文字
        self.page.search.input_keywords("nike")
        # 搜索-点击搜索按钮
        self.page.search.click_search()
        # 搜索-返回
        self.page.search.base_press_back()
        # 删除操作
        self.page.search.click_del_search()
        # 断言搜索历史是否为空
        assert self.page.search.is_search_record_empty()
