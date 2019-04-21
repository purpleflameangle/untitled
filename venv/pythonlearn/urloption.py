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
context = ssl._create_unverified_context()
'''
#get 请求： 一般从指定的服务器请求数据，也有的提交数据给服务器
params = urllib.parse.urlencode({'wd': 'Python get请求'})
print(params)
response = urllib.request.urlopen('http://www.baidu.com/s?%s' % params)
html = response.read().decode('utf-8')
with open('gethtml.html', 'w+') as f:
    f.write(html)


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
#urlopen的Url参数既可以是字符串也可以是Request对象，如果你传入一个字符串，
# 那么Python是会默认先帮你把目标字符串转换成Request对象，然后再传给urlopen函数
response = urllib.request.urlopen(request)
# urlopen实际上返回的是一个类文件对象，因此你可以用read（）方法来读取内容
# geturl()  返回请求的url
# info（） 返回一个httplib.HTTPMessage对象，包含远程服务器返回的头信息
# getcode() 返回HTTP状态码
html1 = response.read().decode('gb2312')
response.close()
print(html1)

#http  header向服务器提交头信息 run success thrid
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

'''
get 与post的区别
http://www.w3school.com.cn/tags/html_ref_httpmethods.asp
GET 请求可被缓存
GET 请求保留在浏览器历史记录中
GET 请求可被收藏为书签
GET 请求不应在处理敏感数据时使用
GET 请求有长度限制
GET 请求只应当用于取回数据

POST 请求不会被缓存
POST 请求不会保留在浏览器历史记录中
POST 不能被收藏为书签
POST 请求对数据长度没有要求

urlopen函数有一个data参数，如果给这个参数赋值，那么HTTP请求就是使用POST方法
如果data的值是NULL,也就是默认值，那么HTTP的请求就是get方式
data参数的值必须符合这个application/x-wwww-form-urlencodec的格式。使用urllib.parse.urlencode()将字符串转换为这个格式
'''

'''
# POST请求：向指定的服务器提交要被处理的数据。
# 请求头添加字符参数内容
# 方法1
data1 = urllib.parse.urlencode({'wd': "Python post request "}).encode('utf-8')
request = urllib.request.Request("http://www.baidu.com/s?")
request.add_header("Content-Type", "application/json")
request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15")
response = urllib.request.urlopen(url=request, data=data1, context=context)
# 确定返回的HTTP状态码
print(response.getcode())


#post 请求 方法2
url2 = 'http://www.baidu.com/s?'
paramsdata = urllib.parse.urlencode({'wd': 'Python post请求'}).encode(encoding='UTF-8')
headers2 = {'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
request = urllib.request.Request(url=url2, data=paramsdata, headers=headers2)
response = urllib.request.urlopen(request, context=context)
result = response.getcode()
print(result)


#http header
request = urllib.request.Request('http://www.example.com/')
request.add_header('Referer', 'http://www.python.org')
urlopen1 = urllib.request.urlopen(request)
print(urlopen1.getcode())


opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
print(opener.open('http://www.example.com/'))
opener.close()
'''

# from https://docs.python.org/3.8/howto/urllib2.html?highlight=httpbasicauthhandler
#创建支持openerdirector的基本的http认证,方法1
# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://mahler:8092/site-updates.py"
username = 'klem'
password = 'kadidd!ehopper'
password_mgr.add_password(None, uri=top_level_url, user=username, passwd=password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
a_url = 'http://www.python.org/'
# opener.open(a_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)
response1 = urllib.request.urlopen(a_url, context=context)
print(response1.getcode())


'''
# Create an OpenerDirector with support for Basic HTTP Authentication...
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.python.org/', context=context)
print(response.getcode())

# soup run success four
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
'''

