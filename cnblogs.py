#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import HTMLTestRunner
import wda
import time
import atx
# help(HTMLTestRunner)
wda.DEBUG = False
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TestCnblogs(unittest.TestCase):
    def setUp(self):

        self.d = atx.connect("http://192.168.11.139:8100", platform='ios')
        self.d.start_app(u"com.yixin.yijiedai")
        self.Errors = []

    def tearDown(self):
        self.d.stop_app()
        self.assertEqual([],self.Errors)



    def bankaddressnull(self):
        u'''用户未设置开户行信息为空'''
        d = self.d
        d(text=u"我").click()
        d(text=u"我").click()
        d(text=u"提现").click()
        d(text=u"立即绑定").click()
        time.sleep(3)
        d(text=u'绑定新的银行卡').click()
        cardholder = d(class_name="TextField").text
        self.assertEqual(u"朱清华",cardholder)


    def tblicai(self):
        u'''用户定期投资100元测试'''
        d = self.d
        d(text=u"理财").click()
        d(text=u"资金存管对接").click()
        d(text=u"我要投标").click()
        tb = d(class_name="TextField")
        tb.click()
        tb.set_text(u'100')
        d(class_name="Button", name=u"完成").click()
        d(text=u"确认投资").click()
        d(text=u"确认支付100元").click()
        time.sleep(3)
        required = d(class_name="StaticText",name="1.00").text
        self.assertEqual(u"1.00",required)







if __name__ == "__main__":
     unittest.main()

















#
# if __name__ == '__main__':
#      unittest.main()