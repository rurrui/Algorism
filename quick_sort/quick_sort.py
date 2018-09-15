# 快速排序

def sort(array):
    if len(array)<2:
        return array
    else:
        position=array[0] # 把数组的一个元素定义为快速排序的基线值
        lessarray=[i for i in array[1:] if i<=array[0]]
        morearray=[j for j in array[1:] if j>array[0]]
        return sort(lessarray)+[position]+sort(morearray)

# 测试
print(sort([4,7,2,9,1,3,8,12,44,77,99,100]))