# 使用递归实现对数组的求和函数

def sum_func(array):
    if len(array)==1:   # 基线条件，当数组只剩一个元素的时候，终止递归，返回当前元素
        return array[0]
    else:
        return array[0]+sum_func(array[1:]) # 递归条件，每次取出数组的第一个元素，剩下的数组再执行递归，直到数组只剩下最后一个元素终止递归

# test
print(sum_func([1,2,3,4,5]))