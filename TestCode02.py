from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
def getTile(url):
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


title = getTile("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print('Title could not be found')
else:
    print(title)
