from base.base_driver import init_driver
from page.page import Page
from time import sleep


class TestClearCache:

    def setup(self):
        self.driver = init_driver(noRest=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_update(self, args):
        # 没有登录,先登录
        self.page.home.login_if_not(self.page)
        # 我-点击设置
        self.page.me.click_setting()
        # 设置-点击清理缓存
        self.page.setting.click_clear_cache()
        # 断言清理成功
        assert self.page.setting.base_estimate_toast_exist("清理成功")