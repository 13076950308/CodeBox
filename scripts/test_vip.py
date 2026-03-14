import time
from base.base_driver import init_driver
from base.base_analyze import analyze_yaml_file
from page.page import Page
from time import sleep
import pytest


class TestVip:

    def setup(self):
        self.driver = init_driver(noRest=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_yaml_file('vip_data.yaml', 'test_vip'))
    def test_vip(self, args):
        keyword = args["keyword"]
        expect = args["expect"]
        # 没有登录,先登录
        self.page.home.login_if_not(self.page)
        # 点击加入超级VIP的选项
        self.page.me.click_be_vip()
        # 切换web环境
        print(self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_com.yunmall.cc")
        # 在VIP页面输入邀请码
        self.page.vip.input_invite(keyword)
        # 点击加入会员按钮
        self.page.vip.click_be_vip()
        # 断言“邀请码不正确”是否在page_source中
        assert self.page.vip.is_keyword_in_page_source(expect), "%s不在page_source中" % expect
        # 切换回原生环境
        self.driver.switch_to.context("NATIVE_APP")



