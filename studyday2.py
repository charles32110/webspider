#coding=utf-8

'''
使用字典池化目标网站
延续第一天get函数
使用[n]对池化的目标内容做切片
依次保存内容在day2[n].html的文件中
延伸for循环对创建文件和写入多个变量的用法
'''
import requests


url_dic = {
    'pythonsite':'http://python.org',
    'openstack':'http://stackoverflow.com',
    'author_site':'https://github.com/charles32110/webspider'
}
def get_content(url):
    resp = requests.get(url)
    return resp.text

a = 0
for i in url_dic.keys():
    print i
    url = url_dic.values()[a]
    content = get_content(url)
    print(content)
    file = open("day2[%d].html" % (a), 'w')
    #file.write(i)
    file.write(i+content.encode('utf-8'))
    file.close()
    a = a + 1