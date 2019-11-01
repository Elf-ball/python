#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import requests
from api.unittest_api import urlpath

class Base(unittest.TestCase):
    """
    可以专门在这里设置一个类，用来继承unittest，后面的测试用例类就可以直接继承这个类了
    这个类里面也可以存放后面用例中需要的参数，如session
    """
    @classmethod
    def setUpClass(cls):
        # 设置测试用例前的准备工作，每个测试类都只会调用一次这个函数
        url = urlpath.url(urlpath.path2)  # 先调用拼接函数，然后再通过urlpath.path2把要拼接的路径找到并传入拼接函数
        # 准备接口测试时需要传递的数据
        data = {
            "username": "xxx",
            "password": "xxx"
        }
        # res = requests.post(url, json=data)
        cls.url = url
