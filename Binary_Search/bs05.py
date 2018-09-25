#

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