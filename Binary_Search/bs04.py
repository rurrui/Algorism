# 中秋节二分查找

def search(l,item):
    start=0
    end=len(l)-1
    while start<=end:
        mid=(start+end)//2
        value=l[mid]
        if value==item:
            return value
        elif value<item:
            start=mid+1
        else:
            end=mid-1
    return None
list1=[1,2,3,4,5,6,7,8,9,10]
item1=10
print(search(list1,item1))
            