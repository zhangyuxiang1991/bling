# coding = utf-8
import time,datetime,logging,os
class base():
    def __init__(self,driver):
        self.driver = driver
    #启动app
    def start(self):
        os.popen('adb shell am start -n cn.percent.dolphin_prod/cn.percent.dolphin.main.activity.WelcomeActivity')
    #关闭app
    def stop(self):
        os.popen('adb shell am force-stop cn.percent.dolphin_prod')
    #清除app缓存
    def clear(self):
        os.popen('adb shell pm clear cn.percent.dolphin_prod')
    #通过id找元素
    def by_id(self,element):
        return self.driver.find_element_by_id(element)

    #通过name找元素
    def by_name(self,element):
        return self.driver.find_element_by_name(element)

    #通过classname找元素
    def by_classname(self,element):
        return self.driver.find_element_by_class_name(element)

    #通过xpath找元素
    def by_xpath(self,element):
        return self.driver.find_element_by_xpath(element)

    #通过css找元素
    def by_css(self,element):
        return self.driver.find_element_by_css_selector(element)
    #等待时间
    def sleep(self,t):
        time.sleep(t)
    #向上滑动
    def swipe_up(self):
        size = self.driver.get_window_size()
        print(size["width"])
        print(size["height"])
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.7, size["width"] * 0.5, size["height"] * 0.3, 500)
    #智能等待
    def find_ele(self,ele, time):
        time1 = datetime.datetime.now()
        tag = False
        while not tag:
            time2 = datetime.datetime.now()
            if (time2 - time1).seconds < time:
                try:
                    self.driver.find_element_by_id(ele).click()
                    print('click ok')
                    tag = True
                except:
                    print("not find")
            else:
                break
    #打印日志信息
    def log(self,message):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                            datefmt='%d %b %Y %H:%M:%S',
                            filename='../Log/'+'logging.log',
                            filemode='a')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

        logging.info(message)