# 使用递归得到一个数组元素的个数

def count_func(array):
    if array==[]:
        return 0
    else:
        return 1+count_func(array[1:])

# test
print(count_func([1,2,3,4,5,6,7,8,9]))