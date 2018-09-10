# 复习二分查找
def search(l1, item):
    start = 0  # 二分查找的起始位置
    end = len(l1) - 1  # 二分查找的终止位置
    while start <= end:  # 只要没有精确地找到值就继续找
        mid = (start + end) // 2
        value = l1[mid]
        if value == item:
            return value
        if value < item:
            start = mid + 1
        else:
            end = mid - 1
    return None


l_test = range(10)
test_value = 8
print(search(l_test, test_value))
