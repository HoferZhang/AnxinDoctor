# -*- coding: utf-8 -*-

import os
import unittest
import config
import time
import common
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

    def test_1_login(self):
        # 确认进入
        print (u'正在进入..')
        self.driver.implicitly_wait(5)
        btn_go = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/login_tv')
        # self.assertEqual('立即进入',go_to.text)
        btn_go.click()

        # 登录
        self.driver.implicitly_wait(5)
        mobile = self.driver.find_element_by_xpath(
            '//android.widget.EditText[@resource-id=\"com.hilficom.anxindoctor:id/edit_text_et\" and @text=\"手机\"]'
        )
        mobile.send_keys(u'12306850060')
        pwd = self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id=\"com.hilficom.anxindoctor:id/password_ll'
            '\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]'
        )
        pwd.clear()
        pwd.send_keys("123456")
        time.sleep(2)

        log_in = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/login_btn')
        log_in.click()
        time.sleep(5)

        # 选择会话列表第一个
        first_session = self.driver.find_element_by_xpath(
            '//android.widget.ListView[@resource-id=\"com.hilficom.anxindoctor:id/inquiry_record_lv\"]'
            '/android.widget.RelativeLayout[1]'
        )
        if first_session.is_enabled():
            first_session.click()

        # 发起随访
        self.driver.implicitly_wait(5)
        contact_patient = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/follow_bt')
        self.assertEqual(u'联系患者', contact_patient.text)
        contact_patient.click()

        self.driver.implicitly_wait(5)
        btn_send = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/send_btn')
        self.assertEqual(u'发送',btn_send.text)
        btn_send.click()

        self.driver.implicitly_wait(5)
        btn_plus = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/plus_other_iv')
        btn_plus.click()

        # 发送照片
        self.driver.implicitly_wait(5)
        btn_pic = self.driver.find_element_by_xpath(
            '//android.widget.LinearLayout[@resource-id=\"com.hilficom.anxindoctor:id/album_ll\"]'
            '/android.widget.ImageView[1]'
        )
        btn_pic.click()
        # 选择照片
        self.driver.implicitly_wait(5)
        pic = self.driver.find_element_by_xpath(
            '//android.widget.GridView[@resource-id=\"com.hilficom.anxindoctor:id/myGrid\"]'
            '/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]'
        )
        pic.click()
        self.driver.implicitly_wait(5)
        btn_done = self.driver.find_element_by_id('com.hilficom.anxindoctor:id/ok_button')
        btn_done.click()
        time.sleep(3)

        # 拍照发送
        btn_plus.click()
        btn_pic_shot = self.driver.find_element_by_xpath(
            '//android.widget.ImageView[@resource-id=\"com.hilficom.anxindoctor:id/imageView\"]'
        )
        btn_pic_shot.click()
        self.driver.find_element_by_id('com.meizu.media.camera:id/switch_camera_btn').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.meizu.media.camera:id/shutter_btn').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.meizu.media.camera:id/btn_done').click()
        time.sleep(3)


# unitest.main()函数用来测试 类中以test开头的测试用例
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(AxDoc)
    unittest.TextTestRunner(verbosity=3).run(suite)