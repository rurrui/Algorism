import time


def ss(l, value):
    for x in l:
        if x == value:
            return value
    return None


L = range(10000000000)
v = 100000000
start_time = time.time()
x = ss(L, v)
end_time = time.time()
print(x)
print(str(end_time - start_time))
