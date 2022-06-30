#!/usr/bin/python
# -*- coding: utf-8 -*-
import pytest
import requests
import allure
from jsonschema import validate
from pytestframe.schema.weather import cd_weather
from pytestframe.pytest_api import urlpath

'''
执行测试用例使用pytest test_api.py命令
'''
@allure.feature("查询天气预报")
class TestApi():

  @allure.story("查询成功天气")
  @pytest.mark.parametrize("city_code",[510100, 500116])
  def test_select_weather(self, login, city_code):
      # 调用公共函数，如登录接口返回的session
      print(f"测试用例{login}")
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
      assert res.status_code == 200
      result = res.json()
      # 对比返回的数据结构是否与自己的预期是相同
      validate(result, cd_weather)

# if __name__ == '__main__':
#     TestApi().test_select_weather()