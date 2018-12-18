# -*- coding: utf-8 -*
"""
介绍urllib和urlilb2
首先安装python对应库，
pip install urllib
pip install urllib2
然后自信学习，打开console 默默输入help查看相关用法，这里文本过多，附上相应官方文档：
 https://docs.python.org/library/urllib
 https://docs.python.org/library/urllib2
"""



import urllib



#get 方法
import urllib2
'''
response = urllib2.urlopen('http://python.org')
data = response.read()
print data
print response.code
'''
def url_respon(url):
    resp = urllib2.urlopen(url)
    return resp.read()
url = 'http://python.org'
data = url_respon(url)
print data
