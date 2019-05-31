# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen


# import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# response = urllib.request.urlopen('https://www.python.org')


'''第一次自己用bs4和request写爬虫'''

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko)Chrome'}
# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
session = requests.session()


# 返回电影相关信息
def movie_info(page):
    print('电影的主链接：%s' % page)
    h = session.get(page, headers=headers)
    soup = BeautifulSoup(h.text, "html.parser")

    # h = urlopen(page)
    # soup = BeautifulSoup(h, 'html.parser')

    # 如果页面不存在，做异常处理 。   **********失败********
    # print(soup)
    # test = soup.find('title').get_text()
    # if test == "页面不存在":
    #     return "movie_athor", " movie_actor", "movie_year", "movie_class"

    result = soup.find('div', {'id': "info"})
    movie_athor_list = []
    movie_actor_list = []
    movie_year_list = []
    movie_class_list = []

    movie_athor = result.span.findAll('a', {'rel': "v:directedBy"})
    for i in range(len(movie_athor)):
        movie_athor_list.append(movie_athor[i].get_text())

    movie_actor = result.findAll('a', {'rel': 'v:starring'})
    for i in range(len(movie_actor)):
        movie_actor_list.append(movie_actor[i].get_text())

    movie_year = result.findAll('span', {'property': 'v:initialReleaseDate'})
    for i in range(len(movie_year)):
        movie_year_list.append(movie_year[i].get_text())

    movie_class = result.findAll('span', {'property': 'v:genre'})
    for i in range(len(movie_class)):
        movie_class_list.append(movie_class[i].get_text())

    return movie_athor_list, movie_actor_list, movie_year_list, movie_class_list


# 主函数
def test_BeautifulSoup(url):
    html = session.get(url, headers=headers)
    # 利用bs4解析网页源代码
    bsOBj = BeautifulSoup(html.text, 'html.parser')

    # 检查编码是否一致
    # print(bsOBj.original_encoding)

    # 找到页面显示电影的模块
    result = bsOBj.find('ol', attrs={'class': "grid_view"})
    # 验证页面源代码
    # print(result)
    # 分别定义存储电影信息的列表
    # 名称
    movie_name_list = []
    # 电影海报
    movie_pic_list = []
    # 标语
    movie_inq_list = []
    # 电影链接
    movie_href_list = []
    # 排名（序号）
    movie_em_list = []
    # 评分
    movie_star_list = []
    # 导演
    athor_list = []
    # 主要演员
    actor_list = []
    # 出品年和国家
    year_list = []
    # 类别
    class_list = []

    # 对电影模块树列进行循环匹配
    for movie_list in result.findAll('li'):
        # 找到电影的名字，加入列表中
        movie_name = movie_list.find(
            'div', {'class': 'hd'}).find('span').get_text()
        movie_name_list.append(movie_name)

        # 找到电影海报，加入列表
        movie_pic = movie_list.find('div', {'class': 'pic'}).find('img')['src']
        movie_pic_list.append(movie_pic)

        # 电影标语
        movie_inq = movie_list.find(
            'p', {'class': 'quote'}).find('span').get_text()
        movie_inq_list.append(movie_inq)

        # 电影链接s
        movie_href = movie_list.find('div', {'class': 'hd'}).find('a')['href']
        movie_href_list.append(movie_href)
        # print(movie_href)

        # 电影排名，加入列表中
        movie_em = movie_list.find(
            'div', {'class': 'pic'}).find('em').get_text()
        movie_em_list.append(movie_em)

        # 电影评分
        movie_star = movie_list.find(
            'span', {'class': 'rating_num'}).get_text()
        movie_star_list.append(movie_star)

        # 保存当前页爬到的图片
        print('当前正在爬取的电影是：%s' % movie_name)
        download_pic(movie_pic, movie_name)
        print('%s的海报图片保存成功' % movie_name)
        print('*****************************************')

        if movie_em in ('20', '27', '122', '123'):
            athor_list.append('movie_athor')
            actor_list.append('movie_actor')
            year_list.append('movie_year')
            class_list.append('movie_class')
        else:
            # 电影制作信息
            movie_athor, movie_actor, movie_year, movie_class = movie_info(
                movie_href)
            athor_list.append(movie_athor)
            actor_list.append(movie_actor)
            year_list.append(movie_year)
            class_list.append(movie_class)

        time.sleep(3)

        '''
        正则表达式，抓取电影制作的相关信息，格式不匹配，一直出现：
        "TypeError: expected string or bytes-like object"的错误异常
        '''
        # 电影制作信息，返回的是一个列表
        # rel = movie_list.find('div', {'class': 'bd'}).find('p').get_text().split()
        # print(rel)

        # res = movie_list.find('div', {'class': 'bd'})
        # print(res)
        # pattern = re.compile(u'主演:(.*?)', re.S)
        # print(re.match(pattern, res))

        # movie = re.match(re.compile('导演:(.*?)'), rel)
        # print(movie)
        # # 制定匹配规则，re.s表示多行匹配
        # pattern = re.compile(u'导演:(.*?)&nbsp;&nbsp;&nbsp;'       # 导演
        #                      + u'主演:(.*?)<br>'                   # 主演
        #                      + u'(.*?)&nbsp;/&nbsp;'               # 年份
        #                      + u'(.*?)&nbsp;/&nbsp;'               # 国家
        #                      + u'(.*?)</p>', re.S)                  # 类别
        # movies = re.findall(pattern, rel)
        # print(movies)
        # for movie in movies:
        #     movie_athor = movie[0].lstrip()
        #     movie_actor = movie[1]
        #     movie_year = movie[2].rstrip()
        #     movie_contry = movie[3]
        #     movie_class = movie[4]
        #     print(movie_athor)
        #     print(movie_actor)
        #     print(movie_year)
        #     print(movie_contry)
        #     print(movie_class)


    '''检查是否查找正确'''
    for i in range(250):
        print('*' * 100)
        print("电影名称：%s" % movie_name_list[i])
        print("电影海报链接：%s" % movie_pic_list[i])
        print("电影豆瓣链接：%s" % movie_href_list[i])
        print("电影排名：%s" % movie_em_list[i])
        print("电影评分：%s" % movie_star_list[i])
        print("电影标语：%s" % movie_inq_list[i])
        print("导演：：%s" % athor_list[i])
        print("电影演员：%s" % actor_list[i])
        print("上映日期和地点：%s" % year_list[i])
        print("电影类别：%s" % class_list[i])
        print('*' * 100)


    # 找到属性class为'title'的标签为span的内容
    # result = bsOBj.findAll('span', {'class' : 'title'})
    # print(result[0])

    # 用css选择器查找(失败)
    # result = bsOBj.select('body>div>div>div>div>ol')
    # print(result)

def download_pic(url, pic_name):  # 下载函数
    name = '/Users/wangwenjun/MyProject/Crawler/Test/' + pic_name + ".jpg"
    print(url)
    print(pic_name)
    if(url is None):  # 地址若为None则跳过
        pass
    result = urlopen(url)  # 打开链接
    # print result.getcode()
    if(result.getcode() != 200):  # 如果链接不正常，则跳过这个链接
        pass
    else:
        data = result.read()  # 否则开始下载到本地
        with open(name, "wb") as code:
            code.write(data)
            code.close()


# 迭代遍历每一页
def page():
    for i in range(0, 10):
        url = 'https://movie.douban.com/top250?start='
        url = url + ('%d' % (i * 25))

        print('\n\n'+'*' * 100)
        print('****************************************爬到的第%d页的数据如下：****************************************' % (i + 1))
        print('*' * 100)

        # 测试单个电影网页不存在的处理
        # url = 'https://movie.douban.com/subject/5912992/'
        # print(url)
        # print(movie_info(url))

        # 正常从主页开始爬
        # print(url)
        test_BeautifulSoup(url)


# 计算爬虫运行时间
def timeup(func):
    start = time.time
    func()
    end = time.time
    timeuse = end - start
    print('\n[%s()]解析一共使用了%d秒时间。\n' % (func.__name__, timeuse))
    return timeuse




def testUrlOpen():
    url = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p462657443.webp'
    name = '/Users/wangwenjun/MyProject/Crawler/Test/' + '测试' + ".jpg"
    if(url is None):  # 地址若为None则跳过
        pass
    result = urlopen(url)  # 打开链接
    # print result.getcode()
    if(result.getcode() != 200):  # 如果链接不正常，则跳过这个链接
        pass
    else:
        data = result.read()  # 否则开始下载到本地
        with open(name, "wb") as code:
            code.write(data)
            code.close()

if __name__ == '__main__':
    timeup(page)
    # testUrlOpen()
