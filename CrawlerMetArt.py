import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import requests
from lxml import etree
import time
import urllib.error

# 生命两个全局变量
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko)Chrome'}
file_path = 'E:\MyProject\Python\JupyterNotebook\爬图片\pic'


# 抓取主页面
def get_url(url):
    html = requests.get(url, headers=headers).text
    file = etree.HTML(html)
    ss = file.xpath('/html/body/div[5]/div[1]/ul/li')
    for s in ss:
        name = s.xpath('./a[1]/img/@alt')[0]
        href = s.xpath('./a[1]/@href')[0]
        print("\n\n一、准备看到模特{},链接是{}".format(name, href))
        # 建模特文件夹名字
        path = make_model_file(name, file_path)
        # 进入相册
        get_photes(href, path)
        time.sleep(1)


# 抓取第二层，模特相册
# 传入模特的链接和模特文件夹路径
def get_photes(url, path1):
    html = requests.get(url, headers=headers).text
    result = BeautifulSoup(html, 'html.parser')
    # 切割页面，去掉视频模块
    r = result.findAll('div', {"class": 'row container custom-content-list'})
    x = r[-1]
    # 找到照片模块列表
    s = x.findAll("li", {"class": "list-group-item"})
    for i in range(len(s)):
        photes_link = s[i].find("div", {"class": "pull-left custom-list-item-detailed-photo"}).find('a').attrs['href']
        photes_name = s[i].find("div", {"class": "pull-left custom-list-item-detailed-photo"}).find('img').attrs['alt']
        print("二、准备看到相册{},链接是{}".format(photes_name,photes_link))
        path3 = make_phote_file(photes_name,path1)
        download_pic(photes_link,path3)
        time.sleep(1)


# 建立模特文件夹，返回模特文件路径
def make_model_file(name,path):
    filename = "{}\{}".format(path,name)
    os.mkdir(filename)
    os.chdir(filename)
    print("*模特名为{}的文件夹已经建立,并转移到该目录下".format(name))
    return filename


# 建立相册文件夹，返回相册路径
def make_phote_file(name, path2):
    filename = "{}/{}".format(path2, name)
    os.mkdir(filename)
    os.chdir(filename)
    print("*相册名为{}的文件夹已经建立,并转移到该目录下".format(name))
    return filename


# 传入相册链接，下载图片
def download_pic(phote_url, filename):
    html = requests.get(phote_url, headers=headers).text
    file = etree.HTML(html)
    img = file.xpath('/html/body/div[5]/div[2]/div/div/ul/li')
    i = 0
    for p in img:
        u = p.xpath('./a/img/@src')[0]
        f = '{}\{}.jpg'.format(filename, i)
        i += 1
        time.sleep(1)
        try:
            result = urlopen(u)
            if (result.getcode() != 200):  # 如果链接不正常，则跳过这个链接
                print("  {}.第{}张图片下载失败，链接被跳过,图片链接是{}".format(i, i,u))
                continue
            else:
                data = result.read()  # 否则开始下载到本地
                with open(f, "wb") as code:
                    code.write(data)
                    code.close()
                    print("  {}.正在下载第{}张图片,图片链接是{}".format(i,i,u))
        except urllib.error.URLError as er1:
            print("  {}.第{}张图片下载失败,异常1！,图片链接是{}".format(i,i,u))
            print(er1.reason)
        except urllib.error.HTTPError as er2:
            print(er2.reason)
            print("  {}.第{}张图片下载失败，异常2,图片链接是{}".format(i,i,u))
        continue
    print("恭喜你：{}这个相册已经下载完毕！！！\n".format(filename))


def main():
    print('*'*20+"爬虫日志"+'*'*20)
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
