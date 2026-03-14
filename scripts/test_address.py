from base.base_driver import init_driver
from base.base_analyze import analyze_yaml_file
from page.page import Page
from time import sleep
import pytest


class TestAddress:

    def setup(self):
        self.driver = init_driver(noRest=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize('args', analyze_yaml_file('address_data.yaml', 'test_address'))
    def test_address(self, args):
        """
        :param args:
        :return:
        """
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我-点击设置
        self.page.me.click_setting()
        # 设置-点击地址管理
        self.page.setting.click_address_list()
        # 地址管理-点击新增地址
        self.page.address_list.click_add_address()
        # 新增地址-输入 收件人
        self.page.edit_address.input_name(name)
        # 新增地址-输入 电话
        self.page.edit_address.input_phone(phone)
        # 新增地址-输入 详细地址
        self.page.edit_address.input_info(info)
        # 新增地址-输入 邮编
        self.page.edit_address.input_post_code(post_code)
        # 新增地址-勾选 设为默认地址
        self.page.edit_address.click_default_address()
        # 新增地址-选择一个随机区域
        self.page.edit_address.choose_region()
        # 新增地址-点击保存
        self.page.edit_address.click_save()
        if toast is None:
            # 断言输入的姓名和电话是否和页面上获取的电话和姓名一致
            assert self.page.address_list.get_default_receipt_name_text() == "%s %s" % (name, phone), "保存成功，默认的姓名与电话与输入的不符"
        else:
            # 断言编辑的页面的toast出现
            assert self.page.edit_address.base_estimate_toast_exist(toast), "保存不成功，toast内容和预期不符"

        # 编辑地址
    def test_edit_address(self):
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我-点击设置
        self.page.me.click_setting()
        # 设置-点击地址管理
        self.page.setting.click_address_list()
        # 如果不存在，则添加地址
        if not self.page.address_list.base_is_feature_exist():
            # 新增地址-输入 收件人
            self.page.edit_address.input_name("Linda")
            # 新增地址-输入 电话
            self.page.edit_address.input_phone("13076950308")
            # 新增地址-输入 详细地址
            self.page.edit_address.input_info("三单元5号")
            # 新增地址-输入 邮编
            self.page.edit_address.input_post_code("558304")
            # 新增地址-勾选 设为默认地址
            self.page.edit_address.click_default_address()
            # 新增地址-选择一个随机区域
            self.page.edit_address.choose_region()
            # 新增地址-点击保存
            self.page.edit_address.click_save()
        # 进入默认地址(进入了edit_address界面)
        self.page.address_list.click_default_address()
        # 重新输入 收件人
        self.page.edit_address.input_name("王五")
        # 重新输入 手机号
        self.page.edit_address.input_phone("18802096038")
        # 重新输入 详细地址
        self.page.edit_address.input_info("岗头中心围村二区10号105")
        # 重新输入 邮编
        self.page.edit_address.input_post_code("518100")
        # 重新输入 所在地区
        self.page.edit_address.choose_region()
        # 点击保存
        self.page.edit_address.click_save()
        # 断言，是否出现“保存成功的toast信息
        assert self.page.address_list.base_estimate_toast_exist("保存成功")

    # 删除地址
    def test_delete_address(self):
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我-点击设置
        self.page.me.click_setting()
        # 设置-点击地址管理
        self.page.setting.click_address_list()
        # 断言是否有地址可删除
        assert self.page.address_list.is_default_feature_exist(), "默认标记不存在，没有地址可以删除"
        # 删除10次地址
        for i in range(10):
            # 点击编辑
            self.page.address_list.click_edit()
            # 判断删除是否存在
            if not self.page.address_list.is_delete_feature_exist():
                # 如果不存在，break
                break
            # 如果存在，则点击删除
            self.page.address_list.click_delete()
            # 点击确定
            self.page.address_list.click_confirm()
            # 点击编辑
            self.page.address_list.click_edit()
            # 点击编辑，断言删除按钮是否存在，如果不存在则通过，如果存在则有问题
            assert not self.page.address_list.is_delete_feature_exist(), "收货地址没有删除完毕"




