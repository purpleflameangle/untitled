# coding = utf-8
import sys as s
import timeit as ti
import urllib.request

print(s.path)
print(ti.__doc__)
print(dir(ti))

response = urllib.request.urlopen("http://www.baidu.com")
html1 = response.read()
print(html1)

# add branch
