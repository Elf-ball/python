#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas
import os


def merge_excel():
    path = "D:\\python_code\\sheet\\"
    fd = []
    # 读取该目录下的文件，并生成列表
    files = os.listdir(path)
    # print(files)
    # 依次读取excel文件，并且把读取的内容添加到空列表中
    for i in files:
        fd.append(pandas.read_excel(path + i, sheet_name='Sheet1'))
    print(fd)
    result = pandas.concat(fd, axis=0)
    print(result)
    # result.to_excel("D:\\python_code\\sheet\\合并后的文件.xlsx", index=0)
    # print(result, '\n')


if __name__ == '__main__':
    merge_excel()
