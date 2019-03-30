# -*- coding: utf-8 -*-
import urllib
import urllib.request
import ssl
import urllib3
import webbrowser
import random

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
print(urllib)
url = "http://www.baidu.com"
data = urllib.request.urlopen(url)
caturl = data.read()
with open('2.jpg', 'wb') as f:
    f.write(caturl)
'''

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
