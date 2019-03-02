# encoding: utf-8
'''
斐波那契数列原理
两个实现方式
1、递归实现
2、非递归方式普通方法实现
'''


def fab(n):
    if n < 1:
        print('input data is error')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)


result = fab(20)
if result != -1:
    print('总共有%d 对兔子诞生' % result)


#不用递归
def fab1(n):
    a1 = 1
    a2 = 1
    a3 = 1
    if n < 1:
        return -1
    if n == 1 or n == 2:
        return 1
    while ( n - 2) > 0:
        a3 = a1 + a2
        a1, a2 = a2, a3
        n -= 1
    return a3


result1 = fab1(20)
if result1 !=1:
    print("20个月后有%d对兔子" % result1)


#阶乘函数

def recursion(n):
    results = n
    for i in range(1, n):
        results *= i
    return results


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


number = int(input('请输入整数：'))
results = recursion(number)
print("%d 的阶乘是：%d" % (number, results))

result2 = factorial(number)
print("%d 的阶乘是：%d" % (number, result2))
