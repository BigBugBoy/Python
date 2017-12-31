# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''bs4解析网页，利用正则查找'''

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'html.parser')
images = bsObj.findAll(
    "img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
