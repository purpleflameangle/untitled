#p9_8.py
def showMaxFactor(num):
    count = int(num) // 2
    while count > 1:
        if num % count == 0:
            print("one")
            print('%d 最大的约数是是 %d' % (num, count))
            break
        count -= 1
    else:
        print('%d 是素数!' % num)


num1 = int(input('请输入：'))
showMaxFactor(num1)

try:
    int('abc')
except ValueError as reason:
    print('出错了：' + str(reason))
else:
    print('没有任何异常')