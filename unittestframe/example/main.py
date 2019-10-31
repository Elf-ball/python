#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittestframe.example.test_mathfunc import TestMathFunc
from BeautifulReport import BeautifulReport


# 在实际运用中，可以把同一模块的所有用例放到一个def中，这样可以方便调试
def mathfunc_suites():
    # unittest.addTest用法
    t_suites = unittest.TestSuite()  # 定义一个测试套件(testsuit)，用来存放将要执行的用例
    t_suites.addTest(TestMathFunc('test_multi'))  # 把需要执行的单个用例添加到测试套件中
    t_suites.addTest(TestMathFunc("test_divide"))  # 同上，用此方法可以把同一模块的用例依次添加进来，并且按照添加的顺序执行
    run = BeautifulReport(t_suites)
    run.report(description="测试报告生成工具",  # 生成的报告右侧，显示的用例名称就是这个参数
               filename="生成的文件名称")


def testloader_suites():
    suites = []  # 构建一个空列表用来装testsuit实例
    testlist = [TestMathFunc]  # 创建一个list用来存储需要执行的测试类
    for testcase in testlist:  # 通过for循环把需要执行的测试类通过Testloader依次加入testsuite
        # 从指定的TestCase构建一个TestSuite对象，该对象包含了TestCase中所有的测试方法
        testsuite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        # 把构建的对象依次传入空列表
        suites.append(testsuite)
    # 把用例装载到测试套件中
    newsuite = unittest.TestSuite(suites)
    run = BeautifulReport(newsuite)
    run.report(description="测试报告生成工具",  # 生成的报告右侧，显示的用例名称就是这个参数
               filename="生成的文件名称")


if __name__ == "__main__":
    # mathfunc_suites()
    testloader_suites()
