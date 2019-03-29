# -*- coding: utf-8 -*-
import sys as s
import timeit as ti
import urllib.request
import urllib.parse
import requests
import uuid
import hashlib

'''
print(s.path)
print(ti.__doc__)
print(dir(ti))

response = urllib.request.urlopen("http://www.baidu.com")
html1 = response.read()
print(html1)
'''
# add branch

'''
使用get方法，这个data参数的值必须符合这个application/x-www-form-urlencoded的格式。
要用urllib.parse.urlencode()将字符串转换成这个格式

# url = "http://fanyi.youdao.com/translate?smartresult = dict&smartresult = rule&smartresult=ugc&sessionFrom = http://www.youdao.com"
url = "http://fanyi.youdao.com/translate?smartresult = dict"
data = {}
data['type'] = 'AUTO'
data['q'] = 'I love FishC.com'
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
# headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
data1 = urllib.parse.urlencode(data).encode('utf-8')
response1 = urllib.request.urlopen(url, data1)
html2 = response1.read().decode('utf-8')
print(html2)

'''

# from youdao api

# reload(sys)
# sys.setdefaultencoding('utf-8')
youdao_url = "http://openapi.youdao.com/api"
# 没有应用KEY和密钥
# APP_KEY = 'YINGYONG id'
# APP_SECRET = '应用密钥'


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size-10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-rulencoded'}
    return requests.post(youdao_url, data=data, headers=headers)


def connect():
    # q = input("请输入要翻译的内容：")
    q = '天亮'
    data ={}
    data['from'] = 'auto'
    data['to'] = 'auto'
    data['signType'] = 'v3'
    # curtime = str(int(time.time()))
    # data['curtime'] = curtime
    salt = str(uuid.uuid1())
    #signstr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    signstr = truncate(q)
    sign = encrypt(signstr)
    #data['appKey'] = APP_KEY
    data['sign'] = sign
    response1 = do_request(data)
    print(response1.content)


if __name__ == '__main__':
    connect()
