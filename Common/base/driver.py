# coding = utf-8
from appium import webdriver

def driver():
    desired_caps = {}
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '6.0.1'
    # 设备号
    desired_caps['deviceName'] = 'emulator-5554'
    # 包名
    desired_caps['appPackage'] = 'cn.percent.dolphin_prod'
    # 启动名
    desired_caps['appActivity'] = 'cn.percent.dolphin.main.activity.WelcomeActivity'
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver