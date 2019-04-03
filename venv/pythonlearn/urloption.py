# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import re
import ssl
from bs4 import BeautifulSoup


'''
keyword = input("请输入关键字：")
keyword1 = urllib.parse.urlencode({"word": keyword})
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
request1 = urllib.request.Request("http://baike.baidu.com/search/word?%s" % keyword1, headers1)
response2 = urllib.request.urlopen(request1)
html = response2.read().decode('utf-8')
'''

# run true
key = input("请输入关键字：")
key = key.encode('utf-8')
url2 = "http://suggestion.baidu.com/su?wd=%s" % key
response = urllib.request.urlopen(url2)
html = response.read().decode('gb2312')
print(html)
with open('proxy1.html', 'w+') as f:
    f.write(html)

