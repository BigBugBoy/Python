# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

from bs4 import BeautifulSoup
from urllib.request import urlopen

'''使用bs4解析网页'''

html=urlopen("http://www.pythonscraping.com/pages/page1.html")
b=BeautifulSoup(html.read(), 'html.parser')
# x=input('请输入：')
# print(x)
print('*'*20)
print(b.html)
print('*'*20)
print(b.head)
print('*'*20)
print(b.body)
print('*'*20)
print(b.h1)
print('*'*20)
print(b.div)
