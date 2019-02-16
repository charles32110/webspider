#coding= utf-8
import urllib
import urllib2
import re
import os
import requests
import threading
import queue
headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language" : "en-us",
  "Connection" : "keep-alive",
  "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"}

def get_content(url):
    resp = requests.post(url,headers=headers,allow_redirects=False)   #allow_redirects设置为重定向
    return resp.text

html = get_content("http://h5.magook.com/?from=bk#/imgr/magazine/639/450360/0")

def getImg(html):
    # 利用正则表达式匹配网页里的图片地址
    pattern = re.compile('<main>.*?class="img-reader-wrap".*?<img.*?<src="//(.*?)">', re.S)
    imglist=re.findall(pattern,html)
    return imglist

print (html)


