from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


# 返回电影相关信息
def movie_info(url):
    h = urlopen(url)
    soup = BeautifulSoup(h, "html.parser")
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

    # 利用bs4解析网页源代码
    html = urlopen(url)
    bsOBj = BeautifulSoup(html, 'html.parser')

    # 检查编码是否一致
    print(bsOBj.original_encoding)
    # 找到页面显示电影的模块
    result = bsOBj.find('ol', attrs={'class': "grid_view"})

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

        # 电影链接
        movie_href = movie_list.find('div', {'class': 'hd'}).find('a')['href']
        movie_href_list.append(movie_href)

        # 电影排名，加入列表中
        movie_em = movie_list.find(
            'div', {'class': 'pic'}).find('em').get_text()
        movie_em_list.append(movie_em)

        # 电影评分
        movie_star = movie_list.find(
            'span', {'class': 'rating_num'}).get_text()
        movie_star_list.append(movie_star)

        # 电影制作信息
        athor_list, actor_list, year_list, class_list = movie_info(movie_href)
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

    # 检查是否查找正确
    print(movie_name_list)
    print(movie_pic_list)
    print(movie_inq_list)
    print(movie_href_list)
    print(movie_em_list)
    print(movie_star_list)
    print(athor_list)
    print(actor_list)
    print(year_list)
    print(class_list)


    # 找到属性class为'title'的标签为span的内容
    # result = bsOBj.findAll('span', {'class' : 'title'})
    # print(result[0])

    # 用css选择器查找(失败)
    # result = bsOBj.select('body>div>div>div>div>ol')
    # print(result)


# 迭代遍历每一页
def page():
    url = 'https://movie.douban.com/top250?start='
    for i in range(10):
        url = url + ('%d' % (i * 25))
        print(url)
        print('*'*50)
        print('爬到的第%d页的数据如下：' % (i+1))
        test_BeautifulSoup(url)
        print('*' * 50)


# 计算爬虫运行时间
def timeup(func):
    start = time.clock()
    func()
    end = time.clock()
    timeuse = end - start
    print('\n[%s()]解析一共使用了%d秒时间。\n' % (func.__name__, timeuse))
    return timeuse


if __name__ == '__main__':
    timeup(page)
