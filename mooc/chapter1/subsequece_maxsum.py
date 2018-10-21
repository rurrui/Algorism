def aaa():

    chn = ('ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu')

    num = input()
    sum = 0
    out_sum = ''

    for i in num:
        sum += int(i)
    for j in str(sum):
        out_sum += chn[int(j)] + ' '
    print(out_sum.rstrip())
aaa()
