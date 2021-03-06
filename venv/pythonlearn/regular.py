#!/usr/bin/python
# -*- encoding: utf-8 -*-
import urllib
import urllib.request
import re
import sys
import os
import ssl


# 正则表达式
# https://docs.python.org/3.6/howto/regex.html?highlight=regular
'''
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    '''
ssl._create_default_https_context = ssl._create_unverified_context

# http_connection.context = ssl.create_default_context(cafile=cfg.ca_certs_file)
# http_connection.context_set = True
print(re.search(r"Fish(C|D)", "FishC"))
# ^表示匹配字符串的开始位置，只有目标字符串出现在开头才会匹配
print(re.search(r"^FishC", "I love FishC.com"))
# $表示匹配字符串的借宿位置，只有目标字符串出现在末尾才会匹配
print(re.search(r"FishC$", "FishC.com!"))
# （）本身是一对元字符串，被他们括起来的正则表达式称为一个子组，为一个整体
#  []它是生成一个字符类，事实上就是一个字符集合，被它包围在里面的元字符都失去了特殊的功能
# 小横杠（-），用它表示范围
# 反斜杠\ 用于字符串转义
# 拖字符^   用于取反
# 表示重复的元字符还有：* ,+ 和?
# 星号（*）表示相当于{0,}
# 加号（+）表示相当于{1,}
# 问号(?) 表示相当于{0,1}
p = re.compile('ab*')
print(p)
p1 = re.compile('ab*', re.IGNORECASE)
print(p1)
p2 = re.compile('[a-z]+')
print(p2)
print(p2.match(''))
m = p2.match('tempo')
print(m)
print(m.group())
print(m.start(), m.end())
print(m.span())

p3 = re.compile(r'\d+')
find = p3.findall('12 drummers drumming, 11 pipers piping')
print(find)

p3 = re.compile('...')
m1 = p3.match('string goes')
if m:
    print('match found:', m1.group())
else:
    print('no match')


p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
print(p.search('Paris in the the spring').group())


m = re.match("([abc])+", "abc")
print(m.groups())

m = re.match("(?:[abc])+", "abc")
print(m.groups())

p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search('(((( Lots of punctuation )))')
print(m.group('word'))

'''
# 获取美图run success
def open_url(url1):
    req = urllib.request.Request(url1)
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15')
    req.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8', 'ignore')
    return html


def get_image(html):
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist = re.findall(p, html)
    try:
        os.mkdir("NewPic")
    except FileExistsError:
        pass
    os.chdir("NewPic")
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)


def get_image1(html):
    p = r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
    imglist1 = re.findall(p, html)
    for each in imglist1:
        print(each)


if __name__ == "__main__":
    url = "http://tieba.baidu.com/p/3823765471"
    get_image(open_url(url))
    url1 = "http://cn-proxy.com/"
    get_image1(url1)
'''