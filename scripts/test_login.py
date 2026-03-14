from base.base_driver import init_driver
from base.base_analyze import analyze_yaml_file
from page.page import Page
from time import sleep
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver(noRest=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_yaml_file('login_data.yaml', 'test_login'))
    def test_login(self, args):
        # 解析yaml的数据
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        # 脚本流程
        # 首页点击我
        self.page.home.click_me()
        # 注册页面点击已有账号去登录
        self.page.register.click_login()
        # 在登录页面输入用户名itheima_text
        self.page.login.input_username(username)
        # 在登录页面输入密码itheima
        self.page.login.input_password(password)
        # 在登录页面点击登录
        self.page.login.click_login()
        # 断言获取输入的用户名是否等于输入的用户名
        if toast is None:
            assert self.page.me.get_nick_name_text() == username, "登录后的用户名与输入的用户名不一致"
        else:
            # 找toast提示，找args中的toast提示是否能找到，如果能则通过，如果不能则不通过
            assert self.page.login.base_estimate_toast_exist(toast)








