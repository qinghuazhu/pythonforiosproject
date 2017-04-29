#!/uer/bin/python
# -*- coding: utf-8 -*-
from cnblogs import TestCnblogs
import time
import HTMLTestRunner
import unittest
testreport = unittest.TestSuite()
testreport.addTest(TestCnblogs("bankaddressnull"))
testreport.addTest(TestCnblogs("tblicai"))
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename ="/Users/QINGHUA/Desktop/htmlrunner/"+now+"_pythonreport.html"
fp = file(filename,"wb")
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"医界贷ios_app测试报告",
        description=u"用例执行情况："
)
runner.run(testreport)
print "写入完毕"