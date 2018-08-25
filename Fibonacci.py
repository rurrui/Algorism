# 生成斐波那契数,这种方法当递归次数多的时候会出现爆栈
def Generate(num):
    if(num==1 or num==2):
        return 1
    return Generate(num-1)+Generate(num-2)
value1=Generate(5)
print(value1)
