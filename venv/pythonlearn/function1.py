# encoding: utf-8
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def zhouchang(self):
        return  (self.x + self.y) * 2

    def Area(self):
        return self.x * self.y


r = Rectangle(4, 5)
print(r.zhouchang())
print(r.Area())


# self cls区别
# self 表示具体的实例本身,如果用类staticmethod,无视此self，当成普通函数
# cls表示这个类本身


class A:
    def b(self):
        print('打印self', self)

    @staticmethod
    def b1():
        print("print b1")

    @classmethod
    def b2(cls):
        print("print cls")


a = A()
print(a.b())
print("--")
print(A.b(a))
print(a.b1())
print(a.b2())


'''
# __init__与__new__比较
# __new__是一个对象实例化的时候所调用的第一个方法
# 类先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self，即self是__new__的返回值
'''


class B:
    def __init__(self):
        print("this is __init__")

    def __new__(cls):
        print("this is __new__", cls)

    def printS(self):
        print("first")
        return print("dfs")


b = B()
b.__init__()
print("1--")
B.__new__(b)
print("2--")
print(b.__init__())
print("3--")
# print(b.__new__())
print("4--")
# print(b.printS())


class C:
    def __init__(self, *args, **kwargs):
        print("init")
        print("print init function")
        return print("print return init %s args: %s kwargs: %s",  self.__class__, *args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print("new")
        print("print new function ", *args, **kwargs)
        return print("print new function %s, args: %s, kwargs: %s", cls.__class__, *args, **kwargs)


c = C('12', '23')
print(c.__init__())
c1 = C('34', '25', "fs")
# print(c.__new__())


class D(object):
    def __init__(self, *args, **kwargs):
        print("init %s" % self.__class__)

    def __new__(cls, *args, **kwargs):
        print("new %s" % cls)
        return object.__new__(cls, *args, **kwargs)


print("object d")
d = D()
# print(type(d))
# print(d.__new__())
