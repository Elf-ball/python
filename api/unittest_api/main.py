#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from api.unittest_api.test_api import API
from BeautifulReport import BeautifulReport

def elf_ball():
    suite = []
    suite_list = [
        API
    ]
    for testcase in suite_list:
        test_suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
        suite.append(test_suite)
    newsuite = unittest.TestSuite(suite)
    return newsuite


if __name__ == '__main__':
    # 把所有执行的测试放入测试套件后，用BeautifulReport输出报告
    t_suite = elf_ball()
    run = BeautifulReport(t_suite)
    # 这里的参数如果不加的话，生成的报告将在执行运行命令的路径下
    run.report(description="apitest",
               filename="api测试报告")
    # 运行命令python -m api.unittest_api.main