# coding = utf-8
from Common.mine.minePage import MinePage
from Common.base.driver import driver
import unittest
class TestMine(unittest.TestCase):
    def setUp(self):
        self.driver = driver()

    #修改用户昵称
    def test01(self):
        change = MinePage(self.driver)
        change.change_nick_name('张宇翔11')


    def tearDown(self):
        #self.driver.quit()
        pass


if __name__=='__main__':
    unittest.main()
