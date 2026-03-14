import allure
import random
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class GoodsListPage(BaseAction):
    # 商品列表 按钮
    goods_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    # 随机点击商品列表
    @allure.step(title="商品列表 随机点击 商品")
    def click_goods(self):
        goods = self.base_find_elements(self.goods_button)
        # 有多少个商品
        goods_count = len(goods)
        # 商品下标
        goods_index = random.randint(0, goods_count-1)
        # 随机取一个商品点击
        goods[goods_index].click()