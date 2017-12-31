from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), 'html.parser')
# text = bsObj.findAll("tr", {"id": {"gift1", "gift3"}})
# print(text)
# text2 = bsObj.findAll("", {"class": "gift"})
# print("*"*20)
# print(text2[1].get_text())
for sibling in bsObj.find("table", {"id": "giftList"}).children:
    print(sibling)
