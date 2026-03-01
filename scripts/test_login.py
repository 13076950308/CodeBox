from base.base_driver import init_driver
from base.base_analyze import analyze_yaml_file
from page.page import Page
from time import sleep
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_yaml_file('contact_data.yaml', 'test_contact'))
    def test_login(self, args):
        print("登录成功")







