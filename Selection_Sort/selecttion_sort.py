# 编写一个返回一个列表中最小值索引的函数
def getminindex(arr):
    minindex = 0  # 最小值的索引
    minvalue = arr[0]  # 最小的值
    for i in range(1, len(arr)):
        if arr[i] < minvalue:
            minvalue = arr[i]
            minindex = i
    return minindex


# 选择排序函数
def sort(arr):
    NewList = []
    for j in range(len(arr)):
        smallindex = getminindex(arr)
        NewList.append(arr.pop(smallindex))
    return NewList


# test
print(sort([5, 4, 3, 2, 1]))
