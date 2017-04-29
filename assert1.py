#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_case.cnblogs import TestCnblogs
import HTMLTestRunner
import unittest

testreport = unittest.TestSuite()

testreport.addTest(TestCnblogs("test_cnblogs_login"))
filename = "workpython projectselenium_pythonreport.html"
fp = file(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"baogao",
        description=u"qk："
)
runner.run(testreport)