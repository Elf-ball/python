#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from unittestfram.example.mathfunc import *


class TestMathFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这里是所有测试用例前的准备工作")

    @classmethod
    def tearDownClass(cls):
        print("这里是所有测试用例后的准备工作")

    @classmethod
    def setUp(cls):
        print("这里是一个测试用例前的准备工作")

    @classmethod
    def tearDown(cls):
        print("这里是一个测试用例后的准备工作")

    @unittest.skip("跳过当前测试用例")
    def test_add(self):
        self.assertEqual(3, add(1, 2))

    def test_minus(self):
        self.skipTest("跳过这个测试用例")
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """测试乘法"""
        self.assertEqual(6, multi(3, 2))

    def test_divide(self):
        """测试除法"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


# if __name__ == "__main__":
#     # 运用main方法可以直接执行当前源文件中的所有测试用例
#     unittest.main(verbosity=1)  # verbosity控制输出错误报告的详细成都，默认1，为0时不输入结果，2则输入详细结果
