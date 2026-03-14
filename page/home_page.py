import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):
    # 我 按钮
    me_button = By.ID, "com.yunmall.lc:id/tab_me"
    # 分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"
    # 购物车
    shop_cart_button = By.ID, "com.yunmall.lc:id/tab_shopping_cart"
    # 搜索放大镜
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 首页
    home_button = By.ID, "com.yunmall.lc:id/tab_home"

    # 点击我
    @allure.step(title="主页 点击 我")
    def click_me(self):
        self.base_click_element(self.me_button)

    # 点击首页
    @allure.step(title="主页 点击 首页")
    def click_home(self):
        self.base_click_element(self.home_button)
        
    # 点击放大镜
    @allure.step(title="主页 点击 放大镜")
    def click_search(self):
        self.base_click_element(self.search_button)

    # 点击分类
    @allure.step(title="主页 点击 分类")
    def click_category(self):
        self.base_click_element(self.category_button)

    # 点击购物车
    @allure.step(title="主页 点击 购物车")
    def click_shop_cart(self):
        self.base_click_element(self.shop_cart_button)

    @allure.step(title="主页 登录 如果没有登录去登录")
    def login_if_not(self, page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        # 没有登录，就去登录
        # 点击已有账号
        page.register.click_login()
        # 输入 用户名
        page.login.input_username("itheima_test")
        # 输入 密码
        page.login.input_password("itheima")
        # 点击登录
        page.login.click_login()


