from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, feature, timeout=30, poll=1.0):
        """
        根据特征，找元素
        :param feature: 特征
        :param timeout:超时时间
        :param poll:频率
        :return:
        """
        element = WebDriverWait(self.driver, timeout, poll). \
            until(lambda x: x.find_element(feature[0], feature[1]))
        return element

    def base_find_elements(self, feature, timeout=30, poll=0.5):
        """
                根据特征，找多个符合特征的元
                :param feature: 特征
                :param timeout:超时时间
                :param poll:频率
                :return:
                """
        elements = WebDriverWait(self.driver, timeout, poll). \
            until(lambda x: x.find_elements(feature[0], feature[1]))
        return elements

    # 点击元素方法封装
    def base_click_element(self, feature):
        self.base_find_element(feature).click()
        # 点击元素方法封装

    # 输入内容封装
    def base_input_content(self, feature, content):
        self.base_find_element(feature).send_keys(content)

    # 清除内容封装
    def base_clear_content(self, feature):
        self.base_find_element(feature).clear()

    # 获取元素的文本内容
    def base_get_content(self, feature):
        return self.base_find_element(feature).text

    # 判断toast是否存在
    def base_estimate_toast_exist(self, message):
        """
        根据部分内容判断toast是否存在
        :param message:部分内容
        :return:是否存在
        """
        message_xpath = By.XPATH, "//*[contains(text, '%s')]" % message
        try:
            self.base_find_element(message_xpath, 5, 0.5)
            return True
        except TimeoutException as e:
            return False

    # 获取toast的文本信息
    def base_get_toast_text(self, message):
        """
        根据部分内容，获取toast上的所有内容
        :param message:部分内容
        :return:所有内容
        """
        message_xpath = By.XPATH, "//*[contains(text, '%s')]" % message
        if self.base_estimate_toast_exist(message):
            return self.base_find_element(message_xpath, 5, 0.5).text
        else:
            raise Exception('toast未出现，请检查参数是否正确或toast有没有出现在屏幕上')

    # 判断某个元素是否存在
    def base_is_feature_exist(self,feature):
        try:
            self.base_find_elements(feature)
            return True
        except TimeoutException:
            return False

    def scroll_page_one_time(self, direction="up"):
        """
        滑动一次屏幕
        :param direction: 方向
        "up":从上往下
        "down":从下往上
        left":从右往左
        "right":从左往右
        :return:
        :param direction:
        :return:
        """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = height / 2
        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y
        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    def find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找某个元素的特征，并且点击
        feature:元素的特征
        :param direction: 方向
        "up":从上往下
        "down":从下往上
        left":从右往左
        "right":从左往右
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.base_find_element(feature)
            except Exception:
                self.scroll_page_one_time(direction)
                if self.driver.page_source == page_source:
                    print('到底了')
                    break
                page_source = self.driver.page_source

    def is_keyword_in_page_source(self, keyword, time_out=10, poll=0.1):
        """
        如果keyword在pagesuorce中那么返回true
        如果keyword不在pagesuorce中那么返回False
        :param keyword: 字符串
        :param time_out: 超时时间，默认为10秒
        :param poll: 频率，默认为0.1秒
        :return:
        """
        end_time = time.time() + time_out
        while True:
            if end_time < time.time():
                return False
            if keyword in self.driver.page_source:
                return True

            time.sleep(poll)

    # 根据特征判断某个元素是否存在
    def is_feature_exist(self, feature):
        try:
            self.base_find_element(feature)
            return True
        except TimeoutException:
            return False

    # 按下返回键
    def base_press_back(self):
        self.driver.press_keycode(4)

    # 按下回车键
    def base_press_enter(self):
        self.driver.press_keycode(66)


