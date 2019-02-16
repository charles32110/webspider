#coding :utf-8

'''
beautifulsoup 摸石头过河

'''
import requests
from bs4 import BeautifulSoup as bs



class movie():

    def __init__(self):
        self.headers ={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) "}


    def pagecontent(self):
        content = requests.get('http://editorial.rottentomatoes.com/guide/best-romantic-comedies-of-all-time/',
                               self.headers).content
        paren = bs(content).find('div',attrs={'class':"articleContentBody"}).prettify()

        #prettify()标准格式输出
        return paren






if __name__=='__main__':
    x = movie()
    print(x.pagecontent())

