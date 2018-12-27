# -*- coding: utf-8 -*
#经过四天的基本学习，我们应该检验一下自己的学习成果，
#下面我们来实战采集豆瓣电影影评的简单爬取: https://movie.douban.com/annual/2018?source=navigation#1   正则表达式
#下一节我们将讲解如何翻页还有解决Unicode的问题


import requests
import re


url = 'https://movie.douban.com/review/best/?app_name=movie'
content = requests.get(url).text
pattern = re.compile('<div data-cid.*?<img.*?title="(.*?)".*?/>.*?<div class="short-content">\n\n(.*?)&nbsp.*?</div>', re.S)
results = re.findall(pattern, content)
for result in results:
    (a , b) = result
    print a,b








