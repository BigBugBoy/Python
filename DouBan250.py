from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re


def test_BeautifulSoup():
    html = urlopen('https://movie.douban.com/top250?start=&filter=')
    bsOBj = BeautifulSoup(html, 'html.parser')

    # 找到页面显示电影的模块
    result = bsOBj.findAll('li')
    print(result)
    # for link in bsOBj.findAll('ol'):
    #     print(link)

    # 找到属性class为'title'的标签为span的内容
    # result = bsOBj.findAll('span', {'class' : 'title'})
    # print(result[0])

    # 用css选择器查找(失败)
    # result = bsOBj.select('body>div>div>div>div>ol')
    # print(result)

# 计算时间


def timeup(func):
    start = time.clock()
    func()
    end = time.clock()
    timeuse = end - start
    print('\n[%s()]解析一共使用了%d秒时间。\n' % (func.__name__, timeuse))
    return timeuse


if __name__ == '__main__':
    timeup(test_BeautifulSoup)
