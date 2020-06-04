# coding = utf-8
from Common.base.basePage import base

class LoginPage(base):
    #BLing获取系统权限时的允许元素
    def allow(self):
        return self.by_id('com.android.packageinstaller:id/permission_allow_button')
    #获取用户名元素
    def username(self):
        return self.by_id('cn.percent.dolphin_prod:id/edit_login_account')
    #获取密码元素
    def password(self):
        return self.by_id('cn.percent.dolphin_prod:id/edit_login_passwogird')
    #获取登录按钮元素
    def loginbtn(self):
        return self.by_id('cn.percent.dolphin_prod:id/login_btn')
    #登录系统
    def loginIn(self,usename,password):
        #清除缓存
        self.log('清除缓存')
        self.clear()
        self.sleep(5)
        self.log('启动程序')
        self.start()
        self.sleep(6)
        #寻找是否有清除缓存
        self.log('允许app访问手机')
        allow = self.allow().get_attribute("enabled")
        if allow:
            self.allow().click()
            self.allow().click()
            self.allow().click()
            self.allow().click()
            self.allow().click()
            self.allow().click()
            self.allow().click()

        self.sleep(3)
        self.log('输入用户名')
        #输入用户名
        self.username().send_keys(usename)
        self.log('输入密码')
        #输入密码
        self.password().send_keys(password)
        self.log('点击登录')
        #点击登录
        self.loginbtn().click()





