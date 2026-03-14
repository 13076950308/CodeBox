from base.base_driver import init_driver
from page.page import Page
from time import sleep


class TestUpdate:

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
        # 设置-点击关于
        self.page.setting.click_about()
        # 关于页面点击“版本更新”
        self.page.about.click_update()
        # 断言当前已是最新版本是否存在
        assert self.page.about.base_estimate_toast_exist("当前已是最新版本")