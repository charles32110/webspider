# -*- coding: utf-8 -*
"""
测试地址池，

建议从
http://www.thebigproxylist.com/
更新，直接下载最新的proxy.txt即可测试，
部分思路源自Author: Yuan Li
看了urllib2直接使用其下面的proxyhandler即可
数量很多，简单测试即可，后面内容我们会带大家完成threads多线程的更多内容
"""

import re
import urllib2

fp=open("/Users/zhangguanqin/PycharmProjects/webspider/webspider/thebigproxylist-18-12-19.txt",'r')
lines=fp.readlines()

for ip in lines:
    try:
            print("当前代理IP "+ip)
            proxy=urllib2.ProxyHandler({"http":ip})
            opener=urllib2.build_opener(proxy,urllib2.HTTPHandler)
            urllib2.install_opener(opener)
            url="http://www.baidu.com"
            data=urllib2.urlopen(url).read().decode('utf-8','ignore')
            print("通过")

            print("-----------------------------")
    except Exception as err:
        print(err)
        print("-----------------------------")


