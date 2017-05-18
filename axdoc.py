# -*- coding: utf-8 -*-

import os
import unittest
import config
import config
from appium import webdriver


class YiDa(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': config.CONNECT['platformName'],
            'platformVersion': config.CONNECT['platformVersion'],
            'deviceName': config.CONNECT['deviceName'],
            'appPackage': config.CONNECT['appPackage'],
            'appActivity': config.CONNECT['appActivity']
        }
        self.driver = webdriver.Remote(config.CONNECT['baseUrl'], desired_caps)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    # 测试脚本
    def test_log_in(self):
        # # 手机登录
        # login_button = self.driver.find_element_by_id('com.hiyee.anxinhealth:id/login_btn')
        # assert isinstance(login_button.is_displayed, object)
        # self.driver.find_element_by_id('com.hiyee.anxinhealth:id/et_content').send_keys("12306050403")
        # self.driver.find_element_by_id('com.hiyee.anxinhealth:id/et_content').send_keys("3334")

        # 微信登录
        self.driver.implicitly_wait(10)
        login_btn_wx_button = self.driver.find_element_by_id('com.hiyee.anxinhealth:id/login_btn_wx')
        self.assertIsNotNone(login_btn_wx_button, '无微信登录入口，请重试')
        login_btn_wx_button.click()

        # 进入微信登陆页面
        self.driver.implicitly_wait(10)
        self.assertIsNotNone(self.driver.find_element_by_class_name('android.widget.FrameLayout'), '未显示微信登录页面')
        self.driver.swipe(500, 1190, 600, 1190, 0.1)
        self.assertIsNotNone(self.driver.find_element_by_id('com.hiyee.anxinhealth:id/image_cb'), '登录失败')

        # print(self.driver.contexts)
        # self.driver.switch_to_window('WEBVIEW_com.tencent.mm')
        # self.driver.find_element_by_id('btnOk').click()


# unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(YiDa)
    unittest.TextTestRunner(verbosity=3).run(suite)