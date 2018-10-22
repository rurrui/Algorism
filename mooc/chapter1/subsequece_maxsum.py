def maxC2(ls, low, upp):
    "divide and conquer"
    if ls is None:
        return 0
    elif low == upp:
        return ls[low]

    mid = (low + upp) // 2  # notice: in the higher version python, “/” would get the real value
    lmax = 0
    rmax = 0
    tmp = 0
    i = mid
    while i >= low:
        tmp += ls[i]
        if tmp > lmax:
            lmax = tmp
        i -= 1
    tmp = 0
    for k in range(mid + 1, upp):
        tmp += ls[k]
        if tmp > rmax:
            rmax = tmp
    return max3(rmax + lmax, maxC2(ls, low, mid), maxC2(ls, mid + 1, upp))


def max3(x, y, z):
    if x >= y and x >= z:
        return x
    return max3(y, z, x)


value = maxC2([3, -1, ], 0, 1)
print(value)
