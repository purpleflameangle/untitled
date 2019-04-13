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


'''
keyword = input("please input:")
keyworden = keyword.encode('utf-8')
keyword1 = urllib.parse.urlencode(keyworden)
request = urllib.request.Request()
# url = "http://www.baidu.com/search/word/df"
response = urllib.request.urlopen("http://www.baidu.com/search/word?%s" % keyword1)
html = response.read()
print(html)




def main():
    # url = "http://www.baidu.com"
    keyword = input("请输入关键字：")
    keyword1 = urllib.parse.urlencode({"word": keyword})
    response1 = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword1)
    html = response1.read()
    soup = BeautifulSoup(html, 'html.parser')
    for each in soup.find_all(href=re.compile('view')):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each['href']])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.load()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, "->", url2])
        print(content)


if __name__ == "__main__":
    main()
'''
