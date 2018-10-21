def recursion(n):
    if n:
        recursion(n-1)
        print(n)


recursion(10)
