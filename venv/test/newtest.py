import requests
import unittest
import urllib3
import json
import sys


def sendData(testData):

    with open('leftside.txt', 'a+') as f:
        f.write(testData['TestId'])
        f.write('-')
        f.write(testData['Title'])
        f.write('\n')
    data = requests.get(testData['Url'],  headers=testData['headers'], data=testData['body'])
    r = data.json()

    with open('result.txt', 'a+') as rst:
            rst.write('返回数据')
            rst.write('|')
        # write test result
            try:
                if cmp(r, testData['Result']) == 0:
                    rst.write('pass')
                else:
                    rst.write('fail')
            except Exception:
                rst.write('no except result')
            rst.write('\n')


if __name__ == "__main__":
    sendData(testData)
