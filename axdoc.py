# -*- coding: utf-8 -*-

import os
import unittest
import common
import config
import time
import logging

from appium import webdriver


class AxDoc(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': config.CONNECT['platformName'],
            'platformVersion': config.CONNECT['platformVersion'],
            'deviceName': config.CONNECT['deviceName'],
            'udid': config.CONNECT['udid'],
            'appPackage': config.CONNECT['appPackage'],
            'appActivity': config.CONNECT['appActivity'],
            'unicodeKeyboard': config.CONNECT['unicodeKeyboard'],
            'deviceReadyTimeout': config.CONNECT['deviceReadyTimeout'],
            'resetKeyboard': config.CONNECT['resetKeyboard']
        }
        self.driver = webdriver.Remote(config.CONNECT['baseUrl'], desired_caps)

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    # 测试脚本
    def test_log_in(self):
        # 确认进入
        self.driver.implicitly_wait(10)
        go_to = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/login_tv')
        # self.assertEqual('立即进入',go_to.text)
        go_to.click()

        # 登录
        self.driver.implicitly_wait(10)
        mobile = self.driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id=\"com.hilficom.anxindoctor:id/edit_text_et\" and @text=\"手机\"]'
        )
        mobile.click()
        mobile.clear()
        mobile.send_keys(u"18500385003")

        self.driver.implicitly_wait(10)
        pwd = self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id=\"com.hilficom.anxindoctor:id/password_ll'
            '\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]'
        )
        pwd.send_keys("111111")
        time.sleep(5)


# unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(AxDoc)
    unittest.TextTestRunner(verbosity=3).run(suite)