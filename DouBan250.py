from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://movie.douban.com/top250?start=&filter=')
bsOBj = BeautifulSoup(html, 'html.parser')
# for link in bsOBj.findAll('ol'):
#     print(link)

