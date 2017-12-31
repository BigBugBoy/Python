# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''bs4解析网页，利用函数findall（）和正则查找'''

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')
for link in bsObj.findAll('div', {'id': 'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
