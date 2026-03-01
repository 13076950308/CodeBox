from appium import webdriver


def init_driver(noRest=True):

    desired_caps = {
                'platformName': 'Android',  # 安卓
                'deviceName': '127.0.0.1:62001',  # 设备名称
                'platformVersion': '12',  # Android版本号
                'appPackage': 'com.yunmall.lc',  # 应用包名
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity',  # 应用界面名
                'udid': '127.0.0.1:62001',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'automationName': 'UiAutomator2',  # 指定使用 uiautomator2
                'noReset': noRest,  # 是否重置应用。True不重置，False重置
                'systemPort': 8201,  # 避免端口冲突
                'adbExec': 'D:\\Program Files\\Nox\\bin\\adb.exe',  # 指定夜神 ADB
                'skipServerInstallation': False  # 跳过自动安装服务（已手动安装
            }

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)