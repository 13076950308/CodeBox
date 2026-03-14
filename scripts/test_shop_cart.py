import time

from base.base_driver import init_driver
from page.page import Page
from time import sleep


class TestShopCart:

    def setup(self):
        self.driver = init_driver(noRest=False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(2)
        self.driver.quit()

    def test_add_shop_cart(self):

        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页-点击分类
        self.page.home.click_category()
        # 分类页面-进入到商品列表
        self.page.category.click_goods_list()
        # 商品列表-进入到商品详情
        self.page.goods_list.click_goods()
        # 记录一下当前商品的标题
        goods_title = self.page.goods_detail.get_goods_title_text()
        # 商品详情点击加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 在商品详情页面选择规格
        self.page.goods_detail.click_spec()
        # 商品的详情-点击购物车
        self.page.goods_detail.click_shop_cart()
        time.sleep(2)
        # 根据添加完成之后的页面，是否有相同的商品标题进行判断
        self.page.goods_detail.is_goods_title_exist(goods_title)

    def test_shop_cart_price(self):
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页点击购物车
        self.page.home.click_shop_cart()
        # 购物车-点击全选
        self.page.shop_cart.click_select_all()
        # 购物车-记录总价
        total_price = self.page.shop_cart.get_total_price()
        # 购物车-点击编辑
        self.page.shop_cart.click_edit()
        # 购物车-点击加号
        self.page.shop_cart.click_add()
        # 购物车-点击完成
        self.page.shop_cart.click_accomplish()
        # 购物车-获取单价
        price = self.page.shop_cart.get_price()
        # 断言 当前总价=记录总价+单价
        assert self.page.shop_cart.get_total_price() == total_price + price

    def test_del_shop_cart(self):
        # 首页如没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页点击购物车
        self.page.home.click_shop_cart()
        # 购物车-判断是否有商品，如果没有则添加
        if self.page.shop_cart.is_shop_cart_empty():

            # 首页-点击分类
            self.page.home.click_category()
            # 分类页面-进入到商品列表
            self.page.category.click_goods_list()
            # 商品列表-进入到商品详情
            self.page.goods_list.click_goods()
            # 记录一下当前商品的标题
            goods_title = self.page.goods_detail.get_goods_title_text()
            # 商品详情点击加入购物车
            self.page.goods_detail.click_add_shop_cart()
            # 在商品详情页面选择规格
            self.page.goods_detail.click_spec()
            # 返回到商品列表页
            self.page.goods_detail.base_press_back()
            time.sleep(2)
            # 返回到商品分类页
            self.page.goods_detail.base_press_back()
            time.sleep(2)
            # 首页点击购物车
            self.page.home.click_shop_cart()

        # 购物车-点击全选
        self.page.shop_cart.click_select_all()
        # 购物车-点击编辑
        self.page.shop_cart.click_edit()
        # 购物车-点击删除
        self.page.shop_cart.click_delete()
        # 购物车-点击确认
        self.page.shop_cart.click_affirm()
        # 断言toast是不是叫做 删除成功
        assert self.page.shop_cart.base_estimate_toast_exist("删除成功")
        # 断言当前页面是不是有一个叫"购物车还是空的"
        assert self.page.shop_cart.is_shop_cart_empty()

