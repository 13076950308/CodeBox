import allure
import random
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class CategoryPage(BaseAction):
    # 商品列表 按钮
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    # 随机点击商品列表
    @allure.step(title="分类 点击 商品列表")
    def click_goods_list(self):
        goods_lists = self.base_find_elements(self.goods_list_button)
        # 有多少个商品
        goods_lists_count = len(goods_lists)
        # 商品下标
        goods_lists_index = random.randint(0, goods_lists_count-1)
        # 随机取一个商品点击
        goods_lists[goods_lists_index].click()