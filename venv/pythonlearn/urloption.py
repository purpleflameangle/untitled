# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import re
import ssl
import json
import sys
from bs4 import BeautifulSoup


print(sys.stdout.encoding)
'''
#  run success one
key = input("请输入关键字：")
key = key.encode('utf-8')
url2 = "http://suggestion.baidu.com/su?wd=%s" % key
response = urllib.request.urlopen(url2)
html = response.read().decode('gb2312')
print(html)
with open('proxy1.html', 'w+') as f:
    f.write(html)


# request run success two
keyword = input("please input:")
#keyworden = keyword.encode('utf-8')
# 服务器地址
url = "http://suggestion.baidu.com/su?wd=%s" % keyword
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html1 = response.read().decode('gb2312')
response.close()
print(html1)



#http post header向服务器提交头信息 run success thrid
keywordheader = input("请输入关键字：")
urlheader = 'http://www.baidu.com/s?wd=%s' %keywordheader
context = ssl._create_unverified_context()
head = {}
head['Content-Type'] = 'application/json'
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
request1 = urllib.request.Request(url=urlheader, headers=head)
response2 = urllib.request.urlopen(request1, context=context)
html = response2.read().decode('utf-8')
with open('proxy2.html', 'w+') as f:
    f.write(html)

'''


#soup run success four
def main():
    # url = "http://www.baidu.com"
    context = ssl._create_unverified_context()
    keyword = input("请输入关键字：")
    keyword1 = urllib.parse.urlencode({"word": keyword})
    response1 = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword1, context=context)
    html = response1.read()
    htmlr = urllib.parse.quote(html)
    soup = BeautifulSoup(htmlr, 'html.parser')
    for each in soup.find_all(href=re.compile('view')):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each['href']])
        response2 = urllib.request.urlopen(url2, context=context)
        html2 = response2.read()
        htmlr2 = urllib.parse.quote(html2)
        soup2 = BeautifulSoup(htmlr2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, "->", url2])
        print(content)


if __name__ == "__main__":
    main()

