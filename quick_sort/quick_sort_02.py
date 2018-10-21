# 复习快速排序算法
def quick_sort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        less = [i for i in a[1:] if i <= pivot]
        greater = [j for j in a[1:] if j > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([4, 6, 1, 4, 9, 11]))
