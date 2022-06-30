#!/usr/bin/python
# -*- coding: utf-8 -*-

host = "https://restapi.amap.com/v3"
weather = "/weather/weatherInfo"  # 高德地图的天气查询接口
path2 = "/xxxxxxxxxxxxxxx"


def url(x):
    # 统一在这里把所有的api拼接好，并返回。这样方便管理
    return host + x
