#coding=utf-8
#字典构建目标池；列表例子
import requests
import os


#formulate the dict
#注意字典类型与json数据类型结构相同，最后一个不要加  '，'  其本意为键值对 {keys:values}
url_dic = {
    'pythonsite':'http://python.org',
    'openstack':'http://stackoverflow.com',
    'author_site':'https://github.com/charles32110/webspider'
}




#formulate list
# #构建列表的形式也可以正常使用requests解析，其内容相当于元组性质
url_list = [
    ('pythonsite','http://python.org'),
    ('openstack','http://stackoverflow.com'),
    ('author_site','https://github.com/charles32110/webspider'),
]


# 使用httpbin看一看构建爬虫的请求信息   例：
r = requests.post('https://httpbin.org/post',data=url_dic)
print r.text






