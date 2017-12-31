# -*- coding: utf-8 -*-
# @Author  : BigBugBoy
# @Software: PyCharm


from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import requests
from lxml import etree
import time
import urllib.error

'''写在前面'''
# 1、采用深度优先算法，抓取MetArt模特相册的照片
# 2、第一步：获取模特链接；第二步：获取相册链接；第三步：下载图片
# 3、利用print将每次重要执行情况反馈到run结果
# 4、设置了计时器，计算程序运行时间

'''需要优化的部分'''
# TODO：
# 1、将code运行日志保存到本地
# 2、做requests请求失败的处理
# 3、图片量比较大，深度爬虫是内存消耗大，可以采用广度优先算法，把当前模特的链接先放到本地，再逐个取出相册的链接放到本地，最后下载

# 申明两个全局变量
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko)Chrome'}
# 设置保存路径
file_path = 'E:\MyProject\Python\JupyterNotebook\爬图片\pic'


# 抓取主页面
def get_url(url):
    html = requests.get(url, headers=headers).text
    # 利用lxml解析HTML
    file = etree.HTML(html)
    # 找到模特板块
    ss = file.xpath('/html/body/div[5]/div[1]/ul/li')
    # 遍历每个模特
    for s in ss:
        # 获得模特名称
        name = s.xpath('./a[1]/img/@alt')[0]
        # 获得模特的相册链接
        href = s.xpath('./a[1]/@href')[0]
        print("\n\n一、准备看到模特{},链接是{}".format(name, href))
        # 在预保存文件夹下创建模特文件夹，并切换到模特目录
        path = make_model_file(name, file_path)
        # 进入相册
        get_photes(href, path)
        # 设置爬虫间隔1秒
        time.sleep(1)


# 抓取第二层，模特相册
# 传入模特的链接和模特文件夹路径
def get_photes(url, path1):
    html = requests.get(url, headers=headers).text
    # 利用bs4解析HTML
    result = BeautifulSoup(html, 'html.parser')
    # 切割页面，去掉头部的视频板块
    r = result.findAll('div', {"class": 'row container custom-content-list'})
    # 有的模特没有单独的视频模块，利用切片-1，取最后一个板块
    x = r[-1]
    # 找到照片模块列表
    s = x.findAll("li", {"class": "list-group-item"})
    for i in range(len(s)):
        # 获得单个相册的链接
        photes_link = s[i].find(
            "div", {
                "class": "pull-left custom-list-item-detailed-photo"}).find('a').attrs['href']
        # 获得单个相册名称
        photes_name = s[i].find(
            "div", {
                "class": "pull-left custom-list-item-detailed-photo"}).find('img').attrs['alt']
        print("二、准备看到相册{},链接是{}".format(photes_name, photes_link))
        # 在模特文件夹内，建立相册文件夹，并切换目录
        path3 = make_phote_file(photes_name, path1)
        # 下载相册照片
        download_pic(photes_link, path3)
        # 设置打开相册间隔时间1秒
        time.sleep(1)


# 建立模特文件夹，返回模特文件路径
def make_model_file(name, path):
    filename = "{}\{}".format(path, name)
    # 创建模特文件夹
    os.mkdir(filename)
    # 切换目录
    os.chdir(filename)
    print("*模特名为{}的文件夹已经建立,并转移到该目录下".format(name))
    return filename


# 建立相册文件夹，返回相册路径
def make_phote_file(name, path2):
    filename = "{}/{}".format(path2, name)
    # 创建相册文件夹
    os.mkdir(filename)
    # 切换目录
    os.chdir(filename)
    print("*相册名为{}的文件夹已经建立,并转移到该目录下".format(name))
    return filename


# 传入相册链接，下载图片
def download_pic(phote_url, filename):
    html = requests.get(phote_url, headers=headers).text
    # 利用lxml解析HTML
    file = etree.HTML(html)
    # 找到照片通用“路径”
    img = file.xpath('/html/body/div[5]/div[2]/div/div/ul/li')
    # 计数器
    i = 0
    # 遍历单个照片链接，并下载到本地
    for p in img:
        u = p.xpath('./a/img/@src')[0]
        # 按照计数器给照片命名
        f = '{}\{}.jpg'.format(filename, i)
        i += 1
        # 设置下载间隔1秒
        time.sleep(1)
        try:
            result = urlopen(u)
            # 如果链接不正常，则跳过这个链接
            if (result.getcode() != 200):
                print("  {}.第{}张图片下载失败，链接被跳过,图片链接是{}".format(i, i, u))
                continue
            else:
                data = result.read()  # 否则开始下载到本地
                with open(f, "wb") as code:
                    code.write(data)
                    code.close()
                    print("  {}.正在下载第{}张图片,图片链接是{}".format(i, i, u))
        # 链接和页面异常
        except urllib.error.URLError as er1:
            print("  {}.第{}张图片下载失败,异常1！,图片链接是{}".format(i, i, u))
            print(er1.reason)
        except urllib.error.HTTPError as er2:
            print(er2.reason)
            print("  {}.第{}张图片下载失败，异常2,图片链接是{}".format(i, i, u))
        # 如果异常，则跳过这个链接
        continue
    print("恭喜你：{}这个相册已经下载完毕！！！\n".format(filename))


def main():
    print('*' * 20 + "爬虫日志" + '*' * 20)
    url = "https://www.metart.com/models/top/"
    get_url(url)
    print('*' * 20 + "结束！！" + '*' * 20)


# 计算爬虫运行时间
def timeup(func):
    start = time.clock()
    func()
    end = time.clock()
    timeuse = end - start
    print('\n\n[%s()]MetArt一共使用了%d秒时间。\n\n' % (func.__name__, timeuse))
    return timeuse


if __name__ == "__main__":
    timeup(main)
