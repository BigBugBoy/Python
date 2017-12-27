from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import os

'''
import requests
import socket
# 设置socket层的超时时间为20秒
socket.setdefaulttimeout(20)
header = {'User-Agent': 'Mozilla/5.0'}

request = requests.session().get(_url, headers=header)
response = urlopen(request)
soup =  BeautifulSoup(response,"html.parser")

# 注意关闭response
response.close()
'''

'''
# 测试新建文件夹。   成功！！！
filename = "haha"
os.mkdir(r'E:\MyProject\%s' %filename)
print("文件夹创建成功")
'''

# 目标网站
url = "https://www.metart.com/models/"

# 下载函数


def download(_url, name):
    if(_url is None):  # 地址若为None则跳过
        pass
    result = urlopen(_url)  # 打开链接
    # print result.getcode()
    if(result.getcode() != 200):  # 如果链接不正常，则跳过这个链接
        pass
    else:
        data = result.read()  # 下载到本地
        with open(name, "wb") as code:
            code.write(data)
            code.close()
    result.close()  # 这么关闭连接是否有意义？？？


# 打开目标地址
html = urlopen(url)
# 实例化一个BeautifulSoup对象
soup = BeautifulSoup(html.read(), 'html.parser')

# 计数
count = 0
# 创建图片链接队列
lst = []
# 创建名字队列
name = []


# 获取标签为img的列表
for link in soup.find_all("li", {'class': 'list-group-item'}):
    # 获取图片地址
    address = link.find('img')['src']
    # 添加到list中
    lst.append(address)
    # 获取模特名称
    name_ = link.find('a', {'class': 'custom-list-item-name'}).get_text()
    name.append(name_)
    # 计数加1
    count += 1


for i in range(count):
    pathName = 'E:\\MyProject\\matart\\' + name[i] + ".jpg"
    download(lst[i], pathName)
    time.sleep(2)
    print("正在下载第：", i+1)
