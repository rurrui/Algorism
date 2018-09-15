# 使用递归实现查找一个数组中的最大值

def max_get(array):
    if len(array)==1:
        return array[0]
    else:
        start_value=array[0]    # 数列的第一个值
        compare_value=array[1]  # 数列的第二个值
        if start_value<compare_value:
            return max_get(array[1:])   # 如果数列的第一个值小于数列的第二个值的话，我们就可以放心的对新数列（也就是从原数列第二个值开始到最后一个元素）进行递归操作
        else:
            array[1]=start_value        # 如果数列的第一个值大于数列的第二个值，就应该把第一个值赋给第二个值再对新数列进行递归操作
            return max_get(array[1:])  

# 测试
print(max_get([9,8,7,6,5,4,3,2,1,100]))  