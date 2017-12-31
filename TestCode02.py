# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

'''bs4解析网页，通过“点”访问子节点'''

def gettile(url):
    try:
        html = urlopen(url)
    except(HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = gettile("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print('Title could not be found')
else:
    print(title)
