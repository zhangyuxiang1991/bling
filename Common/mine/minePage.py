# coding = utf-8
from Common.base.basePage import base
class MinePage(base):
    #获取"我的"元素
    def mine(self):
        return self.by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.LinearLayout/android.widget.TextView')
    #获取"个人信息"元素
    def personal_message(self):
        return self.by_id('cn.percent.dolphin_prod:id/user_info_layout')
    #获取"昵称"元素
    def nick_name(self):
        return self.by_id('cn.percent.dolphin_prod:id/info_right_content')
    #获取修改"昵称"的元素
    def change_nickname(self):
        return self.by_id('cn.percent.dolphin_prod:id/edit_nick_text')
    #进入"我的"页面
    def go_to_mine(self):
        self.mine().click()
    #进入"个人信息"页面
    def go_to_personal_message(self):
        self.personal_message().click()
    #修改昵称
    def change_nick_name(self,nickname):
        self.sleep(3)
        self.log('进入我的页面')
        self.go_to_mine()
        self.sleep(3)
        self.log('进入个人信息页面')
        self.go_to_personal_message()
        self.sleep(3)
        self.log('进入昵称页面')
        self.nick_name().click()
        self.sleep(3)
        self.log('修改昵称')
        self.change_nickname().send_keys(nickname)

