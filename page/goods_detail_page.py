import allure
import time

from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):
    # 加入购物车 按钮
    add_shop_cart_button = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"
    # 确认按钮
    confirm_button = By.XPATH, "//*[@text='确认']"
    # 商品标题
    goods_title_text_view = By.ID, "com.yunmall.lc:id/tv_product_title"
    # 购物车按钮
    shop_cart_button = By.ID, "com.yunmall.lc:id/btn_shopping_cart"

    # 点击加入购物车
    @allure.step(title="商品详情 点击 添加购物车")
    def click_add_shop_cart(self):
        self.base_click_element(self.add_shop_cart_button)

    # 点击确认
    @allure.step(title="商品详情 点击 确认")
    def click_confirm(self):
        self.base_click_element(self.confirm_button)

    # 获取“请选择 分类 规格 获取 请选择后面的第一个规格的名字
    @allure.step(title="商品详情 获取 第一个规格的词语")
    def get_choose_spec(self, text):
        return text.split(" ")[1]

    # 选择规格
    @allure.step(title="商品详情 选择 规格")
    def click_spec(self):
        while True:
            # 先点击确认的按钮
            self.click_confirm()
            if self.base_estimate_toast_exist("请选择"):
                spec_name = self.get_choose_spec(self.base_get_toast_text("请选择 "))
                # xpath取父节点的第二个元素
                spec_feature = By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.base_click_element(spec_feature)
                time.sleep(2)
            else:
                break

    # 获取商品的标题
    @allure.step(title="商品详情 获取 商品标题")
    def get_goods_title_text(self):
        return self.base_find_elements(self.goods_title_text_view)

    # 点击购物车按钮
    @allure.step(title="商品详情 点击 购物车")
    def click_shop_cart(self):
        self.base_click_element(self.shop_cart_button)

    # 根据商品的标题判断是否存在这个页面上
    @allure.step(title="商品详情 判断 商品标题是否存在")
    def is_goods_title_exist(self, title):
        title_xpath = By.XPATH, "//*[@text='%s']" % title
        return self.is_feature_exist(title_xpath)


        