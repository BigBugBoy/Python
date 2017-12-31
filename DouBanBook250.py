import requests
from lxml import etree
import time
with open('E:/MyProject/Python/book250.csv', 'w', encoding='utf-8') as f:
    for a in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(a * 25)
        data = requests.get(url).text
        s = etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
        for div in file:
            title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
            pf = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
            scrib = div.xpath('./tr/td[2]/p[2]/span/text()')
            num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')').strip()
            href = div.xpath('./tr/td[1]/a/@href')[0]
            time.sleep(1)
            if len(scrib) > 0:
                f.write('{},{},{},{},{}\n'.format(title, pf, num, href, scrib[0]))
            else:
                f.write('{},{},{},{}\n'.format(title, pf, num, href))
        print("*********正在写入第{}页图书*********".format(a+1))

            # 输出验证
            # if len(scrib) > 0:
            #     print('{} {} {} {} {}'.format(title, pf, num, href, scrib))
            # else:
            #     print('{} {} {} {}'.format(title, pf, num, href))
