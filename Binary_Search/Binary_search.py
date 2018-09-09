# -*- coding: utf-8 -*-

import time


# 实现一个二分查找算法的函数
# L：查询的列表对象
# Item：查询的对象
def bf(l, item):
    start = 0  # 定义一个查询的起始位置
    end = len(l) - 1  # 定义一个查询的终止位置
    while start <= end:
        mid = (start + end) // 2
        value = l[mid]
        if item == value:
            return value
        if item < value:
            end = mid - 1
        else:
            start = mid + 1
    return None


test1 = range(100000000000000000)
test2 = 10000000000000000
start_time_binary = time.time()
x = bf(test1, test2)
print(x)
end_time_binary=time.time()
print(str(end_time_binary-start_time_binary))
