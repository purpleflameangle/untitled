# encoding: utf-8
import random as r
'''
检查信息：如果在类、定义它的类的后代或模块之外访问受保护的成员，则此检查会发出警告。
'''


class Pers(object):
    def __init__(self):    #私有变量定义需要用—__init__,生效时曾现紫色,需要在命名空间下第一行
        self.__name1 = ['这是似有函数']
        #print('私有函数')

    def add(self,param):
        self.__name1.append(param)

    def name(self):
        print(self.__name1)


p = Pers()

print(p._Pers__name1)
p.add('添加')
print(p._Pers__name1)


class A():
    def __init__(self):
        self.__name = 'python'


class B(A):
    def pr(self):
        print(self.__name)


a = A()
b = B()
print(b._A__name)


class C():
    def __init__(self):
        self.__name = 'fs'


class C(C):
    def pr(self):
        print("print")


c = C()
c.pr()
print(c.pr())


#p112
class Fish(object):
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x -= 1
        print("一路向西走坐标", self.x, self.y)


class Goldfish(Fish):
    pass


class Crap(Fish):
    pass


class Salmon(Fish):
    pass


class Shark(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("鲨鱼还没有吃饱")
            self.hungry = False
        else:
            print('鲨鱼吃饱了')


fish = Fish()
fish.move()
g = Goldfish()
g.move()
c = Crap()
c.move()
s = Shark()
s.eat()
s.eat()


class Shark1(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry = True


s1 = Shark1()
s1.move()


#super自动寻找基类
class Shark2(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True


s2 = Shark2()
s2.move()


class Base1:
    def fool(self):
        print("我是fool，我在base1中")


class Base2:
    def fool2(self):
        print("我是foll，我在base2中")


class Base3:
    def fool3(self):
        print("我是fool2，我在base3中")


class C(Base1, Base2, Base3):
    pass


c = C()
c.fool()
c.fool2()
c.fool3()


#组合p11-3
class Turtle:
    def __init__(self, x):
        self.num = x


class Fish3:
    def __init__(self, y):
        self.num = y


class Pool(Turtle, Fish3):
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish3(y)

    def printp(self):
        print("Pool have %d Turtle and  %d Fish" % (self.turtle.num, self.fish.num))


p = Pool(1, 9)
p.printp()


class D:
    count = 0


d = D()
e = D()
f = D()
#对实例对象c的count属性进行赋值后，就相当于覆盖了类对象C的count属性。
#如果没有赋值覆盖，那么引用的是类对象的count属性
#类中定义的属性是静态变量，也就是相当于C语言中加上static关键字声明的变量，类的属性是与类对象进行绑定，
#并不会依赖任何他的实例对象
print(d.count, e.count, f.count)
f.count += 10
print(d.count, e.count, f.count)
D.count += 100
print(d.count, e.count, f.count)
