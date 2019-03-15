# encoding: utf-8
import time as t


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

# ----------------------------------------------------


class CreateObject:
    def __init__(self):
        # 对象－创建完就会调用
        print("对象初始化")

    def __new__(cls, *args, **kwargs):
        print("创建对象")
        return '1'  # 会将返回值提供给引用对象变量


e = CreateObject()
print(e)
# 不按系统方式创建对象,返回对象'1',就不会调用_init_方法




class NewInit1(object):
    def __new__(cls, *args, **kwargs):
        # Called when creating an object
        print("create object")
        # 返回默认的父类object通过__new__方法创建的对象，即通过系统的方式创建的对象
        return object.__new__(cls)

    def __init__(self):
        print("Objects are called as soon as they are created")
        print("Object initialization")


newinit1 = NewInit1()
print(newinit1)


'''
(1)_new_方法是在创建对象时调用的;

_init_方法是在对象一创建完就调用,而且只有通过系统的方法创建的对象才会执行_init_方法,object默认的_new_方法会先于_init_方法调用

(2)_new_方法的形参是类,而_init_方法的形参是对象

"""类方法"""
# class Dog:
#     __type = "狗"  # 类属性
#
#     #  类方法: 和类属性配合使用,想要访问或者修改类属性时,可以定义类方法
#     @classmethod  # 方法上边添加 @classmethod 标识,就会自动生成类方法
#     def get_type(cls):  # 类方法会自动设置第一个形参为cls,调用时自动设置类对象为第一个实参
#         return cls.__type

'''


class F(object):
    __type = 'lei'

    def __new__(cls, *args, **kwargs):
        print("创建对象时调用,用于创建对象")
        return cls.__type

    def __init__(self):
        print("创建完成对象后 才会调用，拥有初始化")


f = F()
print(f)
# --------------------------------------------


class MyTimer:

    def start(self):
        self.start = t.localtime()
        print("time start")
        # return self.start


    def stop(self):
        self.stop = t.localtime()
        self.calc()
        print("time stop")
        #return self.stop

    def calc(self):
        self.last = []
        self.promp = "总共计时了 "
        for index in range(6):
            self.last.append(self.stop[index] - self.start[index])
            self.promp += str(self.last[index])
        print(self.promp)


mt = MyTimer()
mt.start()

mt.stop()


class E:
    def __init__(self, size=10):
        self.size = size

    def getsize(self):
        return self.size

    def setsize(self, value):
        self.size = value

    def delsize(self):
        del self.size

    getpre = property(getsize, setsize, delsize)


e = E()
e.getpre = 12
print(e.getpre)
# del e.getpre
# print(e.getpre)


# 描述符property
'''
class MyProperty:
    def __get__(self, instance, value):
        print("获取属性", self, instance, value)

    def __set__(self, instance, value):
        print("设置属性值", self, instance, value)

    def __delete__(self, instance):
        print("删除数据", self, instance)


class MyProperty1:
    x = MyProperty()


mp = MyProperty1()
print(mp.x)
mp.x = 'x-man'

del mp.x
'''


class MyProperty2:

    def __init__(self, getx=None, setx=None, fdelx1=None):
        self.getx = getx
        self.setx = setx
        self.fdelx1 = fdelx1  # abc

    def __get__(self, instance, owner):
        return self.getx(instance)

    def __set__(self, instance, value):
        self.setx(instance, value)

    def __delete__(self, instance):
        self.fdelx1(instance)


class G:
    def __init__(self):
        self._gx = None

    def getx(self):  # abc
        return self._gx

    def setx(self, value):
        self._gx = value

    def delx(self):
        del self._gx
       # print("df")

    x = MyProperty2(getx, setx, delx)


g = G()
print(g)
# print(g.x('df'))


class CountList:
    def __init__(self, *args):
        self.value = [i for i in args]
        self.count = {}.fromkeys(range(len(self.value)), 0)

    def len(self):
        return len(self.value)

    def fs(self, key):
        self.count[key] += 1
        return self.value[key]


cl = CountList(1, 2, 3, 4)
print(cl.value)
print(cl.count)
