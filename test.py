#!/usr/bin/python
# -*- coding: UTF-8 -*-

''''
ios 自动化测试脚本api练习

'''
import wda
import time
import atx

wda.DEBUG = False

#d = atx.connect("http://192.168.11.139:8100")
d = atx.connect("http://192.168.11.139:8100",platform='ios')
d.start_app("com.yixin.yijiedai")
# d(text=u'计时器').click()
# d(text=u'开始计时').click()
# d(text=u'取消').click()
# d.stop_app()
# d(text=u'允许').click()
# time.sleep(5)
# d.swipe(300, 400, 100, 400, 100)
print "来到这里"
# for i in range(4):
#     time.sleep(2)
#     d.swipe(700, 900, 100, 900, 0.4)
#     print i,'次'
# time.sleep(2)
# d(text=u'立即体验').click()
d(text=u'我').click()
# d(text=u'我').click()
# elem = d(text=u'请输入用户名/手机号')
# elem.click()
# elem.set_text('tzqh')
# d(text=u'下一步').click()
# #time.sleep(3)
# pwd = d(class_name="SecureTextField",value=u"请输入登录密码")
# pwd.click()
# pwd.set_text(u'123456')
# d(text=u'登录').click()
d(text=u'提现').click()
d(text=u'立即绑定').click()
time.sleep(3)
# elemt = d(text=u'绑定新的银行卡').text
# print elemt
d(text=u'绑定新的银行卡').click()
cardholder = d(class_name="TextField").text
print cardholder

# d(text=u"理财").click()
# d(text=u"资金存管对接").click()
# d(text=u"我要投标").click()
# tb = d(class_name="TextField")
# tb.click()
# tb.set_text(u'100')
# d(class_name="Button", name=u"完成").click()
# d(text=u"确认投资").click()
# d(text=u"确认支付100元").click()
# time.sleep(3)
# yl = d(class_name="StaticText", name="1.00").text
# print yl



















# d(text=u'绑定新的银行卡').click()
# card = d(text=u'银行卡号')
# card.click()
# no = d(class_name="TextField",value=u"请输入银行卡号")
# no.set_text(u"445891199109898790")
# d(text=u'选择银行').click()
# # # for i in range(100):
# # #     d.swipe(300, 900, 300, 800, 0.3)
# # #     print i,'次'
#
# d(text=u"天津银行(企业)").scroll().click()

# dis = d.display
# print dis.width,dis.height
# d(text=u'招商银行').click()
# d(text=u'银行卡资料').click()
# d(text=u'开户行所在地').click()
# d(text=u'确定').click()
# address = d(class_name="TextField",value=u"请输入开户支行名称")
# address.click()
# address.set_text(u'广东省云浮市罗定市三江镇')
# d(text=u'开户支行').click()
# rmobile = d(class_name="TextField",value=u"请输入预留手机号")
# rmobile.click()
# rmobile.set_text(u'18817450650')
# d(text=u'预留手机号').click()
# d(text=u'下一步').click()






# print '滑动一次'





# wda.DEBUG = False
# wda.HTTP_TIMEOUT = 600
# #
# # #show status
# c = wda.Client('http://192.168.11.139:8100')
# # #print c.status()
# #
# #
# # #open app
# with c.session('com.yixin.yijiedai') as s:
#  	print s.orientation





#time.sleep(15)

#截图
#c.screenshot('screen.png')
# c.healthcheck()
# c.home()
# #c.session()
#
# c.source() # format XML
# c.source(accessible=True)
#
# print s.bundle_id, s.id
#
# print '测试这里'

# print s.window_size()
# try:
#     print s.orientation
#
# except Exception as E:
#     E.message



#点击某个坐标
# s.tap_hold(100, 20, 1.0)