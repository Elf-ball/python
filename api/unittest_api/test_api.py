#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from api.schema.weather import cd_weather
from api.unittest_api import urlpath
from api.unittest_api.base import Base
from jsonschema import validate
from parameterized import parameterized


class API(Base):

    @parameterized.expand([  # 使用不同的参数多次执行此用例
        ("510100",),
        ("500116",)
    ])
    def test_select_weather(self, city_code):
        """测试高德地图查询天气接口"""
        url = urlpath.url(urlpath.weather)  # 拼接想要测试的接口
        data = {
            "key": "95f5a2b5e0aab802f07c5d4c91afc4cc",  # 高德地图开发者账户中申请的key
            "city": city_code,  # 城市的code，由高德地图提供
            "extensions": "base",
            "output": "json"  # 期望返回的数据类型
        }
        res = requests.get(url, params=data)  # 使用get请求获取城市的天气情况
        print(res.json())
        self.assertEqual(200, res.status_code)  # 判断返回的状态码是否于与自己的期望一致
        result = res.json()
        # 对比返回的数据结构是否与自己的预期是相同
        validate(result, cd_weather)


# if __name__ == '__main__':
# #     API().test_select_weather()
