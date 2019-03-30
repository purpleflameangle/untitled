# -*- coding: utf-8 -*-
import urllib
import urllib.request
import ssl
import urllib3
import webbrowser
import random
from bs4 import BeautifulSoup
import re


def openbrowser(url2):
    webbrowser.open(url2)


def ranname():
    r = ['q', 'w', 'e', 'r']
    r1 = ['q', 'w', 'e', 'r']
    for i in range(2):
        name = random.choice(r) + random.choice(r1)
    htmlname = 'proxy_%s.html' % name
    return htmlname


def writehtml(htmlone):
    with open('proxy.htm', 'w+') as f1:
        f1.write(htmlone)


ssl._create_default_https_context = ssl._create_unverified_context

'''

# 首先data数据转换为utf－8，接着request请求URL和data(req=urllib.request.request(url,data))，
# 然后加上header，请求打开urlopen(urllib.request.urlopen()，可以读取请求的数据（response.read())
# 可以考虑json.load('上面获取的数据html'）
print(urllib)
url = "http://www.baidu.com"
data = urllib.request.urlopen(url)
caturl = data.read()
with open('2.jpg', 'wb') as f:
    f.write(caturl)

#使用代理

# url1 = 'https://www.whatismyip.com/'
url1 = 'https://www.whatismyip.com/'
proxy_support = urllib.request.ProxyHandler({'http': '111.177.191.242:9999'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
req = urllib.request.Request(url=url1, headers=headers1)
response2 = urllib.request.urlopen(req)
html = response2.read().decode('utf-8')
writehtml(html)
# print(html)



url2 = 'http://www.whatismyip.com/'
print("添加代理ip地址，多个地址用英文分号隔开")
iplist = input("请开始输入：").split(';')
while True:
    # 代理参数是一个字典，字典的键是代理的类型，例如http，ftp，字典的值就是代理的IP地址和对应的端口号
    ip = random.choice(iplist)
    proxy_support = urllib.request.ProxyHandler({'http': ip})
    # opener 可以看作是一个私人定制，给予给定的headers，或者给他定制指定的代理IP
    opener = urllib.request.build_opener(proxy_support)
    opener.addheader = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15')]
    urllib.request.install_opener(opener)
    try:
        print("正在尝试使用%s 访问..." % ip)
        response = urllib.request.urlopen(url2)
    except urllib.error.URLError:
        print('访问出错！')
    else:
        print("访问成功")
    if input("请问是否继续?(Y/N):") == 'N':
        break
'''

url3 = "http://baike.baidu.com/view/284853.htm"
response3 = urllib.request.urlopen(url3)
html = response3.read()
soup = BeautifulSoup(html, "html.parser")
for each in soup.find_all(href=re.compile("view")):
    print(each.text, "->", ''.join(["http://baike.baidu.com", each["href"]]))

