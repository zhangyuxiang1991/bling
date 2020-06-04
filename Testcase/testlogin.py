# coding = utf-8
import unittest,HTMLTestRunner,os,time
from Common.base.loginPage import LoginPage
from Common.mine.minePage import MinePage
from Common.base.driver import driver
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver()
    #输入号码和密码，登录系统
    def test01(self):
        lo = LoginPage(self.driver)
        lo.loginIn('18768175067','zyx512168')
        time.sleep(3)
        #断言是否登录成功
        #self.assertEqual(self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView').text,"我的",msg="登录失败")

    # 修改用户昵称
    def test02(self):
        change = MinePage(self.driver)
        change.change_nick_name('张宇翔11')

    def tearDownClass(cls):
        pass


if __name__=='__main__':
#    unittest.main()
    #构造测试套件
    suite = unittest.TestSuite()
    suite.addTest(TestLogin('test01'))
    suite.addTest(TestLogin('test02'))
    #执行测试
    #runner = unittest.TextTestRunner(verbosity=2)
    filename = r'/Users/zhangyuxiang/Software/Pycharmprojects/BLing/Report/report.html'
    fp = open(filename,'wb',encoding='uft-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='单元测试报告',description='单元测试')
    runner.run(suite)
    fp.close()


