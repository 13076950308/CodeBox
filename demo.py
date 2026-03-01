import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
                'platformName': 'Android',  # 安卓
                'deviceName': '127.0.0.1:62001',  # 设备名称
                'platformVersion': '12',  # Android版本号
                'appPackage': 'com.android.settings',  # 应用包名
                'appActivity': 'com.android.settings.Settings',  # 应用界面名
                'udid': '127.0.0.1:62001',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'automationName': 'UiAutomator2',  # 指定使用 uiautomator2
                'noReset': True,  # 是否重置应用。True不重置，False重置
                'systemPort': 8201,  # 避免端口冲突
                'adbExec': 'D:\\Program Files\\Nox\\bin\\adb.exe',  # 指定夜神 ADB
                'skipServerInstallation': False  # 跳过自动安装服务（已手动安装
            }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)








