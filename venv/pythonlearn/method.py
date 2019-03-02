class A(object):
    def __init__(self):
        self.__data = ['dfs']  # 翻译成 self._A__data=[]

    def add(self, item):
        self.__data.append(item)  # 翻译成 self._A__data.append(item)

    def printData(self):
        print("fg")
        self.__data  # 翻译成 self._A__data


a = A()
a.add('hello')
a.add('python')
#a.printData()
# print a.__data  #外界不能访问私有变量 AttributeError: 'A' object has no attribute '__data'
print(a._A__data)  # 通过这种方式，在外面也能够访问“私有”变量；这一点在调试中是比较有用的！
