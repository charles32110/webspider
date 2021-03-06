#coding= utf-8

"""
    自学python笔记day1
    requests库基本使用方法
    为什么要百度问别人呢，直接使用help参数，查看原汁文档
    Requests HTTP Librar

    Requests is an HTTP library, written in Python, for human beings. Basic GET
    usage:

       >>> import requests
       >>> r = requests.get('https://www.python.org')
       >>> r.status_code
       200
       >>> 'Python is a programming language' in r.content
       True

    ... or POST:

       >>> payload = dict(key1='value1', key2='value2')
       >>> r = requests.post('https://httpbin.org/post', data=payload)
       >>> print(r.text)
       {
         ...
         "form": {
           "key2": "value2",
           "key1": "value1"
         },
         ...
       }

"""
#使用get方法获得目标网页信息内容及其长度
import requests


def get_content(url):
    resp = requests.get(url)
    return resp.text

url = "http://h5.magook.com/?from=bk#/imgr/magazine/639/450360/0"
content = get_content(url)
print(content)

content_len = len(content)
print(content_len)

#顺便保存个html吧
f1 = open('day1.html','w')
f1.write(content)
f1.close()