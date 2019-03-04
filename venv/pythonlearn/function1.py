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


# 类先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self，即self是__new__的返回值
# __init__与__new__比较
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
print(b.printS())
