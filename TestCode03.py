# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

from urllib.request import urlopen
from bs4 import BeautifulSoup

'''bs4解析网页，函数find（）找到第一个节点，访问其子节点'''

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), 'html.parser')
# text = bsObj.findAll("tr", {"id": {"gift1", "gift3"}})
# print(text)
# text2 = bsObj.findAll("", {"class": "gift"})
# print("*"*20)
# print(text2[1].get_text())
for sibling in bsObj.find("table", {"id": "giftList"}).children:
    print(sibling)
