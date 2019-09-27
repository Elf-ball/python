#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListOperating(object):
    def deduplication(self):
        """list中数据去重"""
        list_number = [1, 5, 1, 11, 3, 5]
        format_list = []
        for number in list_number:  # 对数组进行迭代，把所有的元素取出来
            if number not in format_list:  # 判断取出来的元素是否已被添加到此列表
                format_list.append(number)  # 把未添加进此列表的元素添加进来
        print(format_list)
        print(min(list_number))  # 找出列表中最小的值


if __name__ == "__main__":
    ListOperating().deduplication()
