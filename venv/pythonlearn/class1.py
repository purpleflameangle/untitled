class ball:
    def setName(self, name):
        self.name=name
    def kick(self):
        print("kick的属性 %s " % self.name)


a = ball()
a.setName("df")

b = ball()  #实例化
b.setName("shuchu")
b.kick()



#公有变量访问
class gyoubianliang:
    name = "公有变量"
    def gff(self, names):
        self.name = names


p = gyoubianliang()
print(p.name)

'''
#私有对象和方法的访问
class Person:
    def __ini__(self, name):
        self.__name = name
        print("调用私有变量")

    def setName(self):
        print("调用设置名字")
        return self.__name


p = Person()
print(p.setName())

'''


class Person(object):
    __names = "private bianliang"

    def __ini1__(self):
        self.__name = ['xiaoDF']
        print("私有方法")

    def getName(self):
        print("getName")
        #self.__name
        #return self.__name
        print(self.__name)

#    def getName(self):
#        return self.__name


p = Person()
print(p._Person__name)
print(dir(Person))

#print(p.__dict__)
print(p.__Person__name)
