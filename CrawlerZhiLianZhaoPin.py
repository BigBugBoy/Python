import requests
from lxml import etree
import time
# url= 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=5002000&sj=618%3b127%3b780%3b619%3b778%3b620%3b779&in=140000&jl=上海&isadv=0&sg=0b2bd876a05e404397437240dd267b98&p=1/'
# 上海、广州4 页数据；北京11页数据；武汉2页；深圳4页；杭州3页；沈阳2页
u = []
city = ['上海', '广州', '北京', '武汉', '深圳', '杭州', '沈阳', '长春']
page = [4, 4, 11, 2, 4, 3, 2, 1]
for i in range(8):
    for k in range(page[i]):
        u.append('http://sou.zhaopin.com/jobs/searchresult.ashx?bj=5002000&sj=618%3b127%3b780%3b619%3b778%3b620%3b779&in=140000&jl={}&isadv=0&sg=0b2bd876a05e404397437240dd267b98&p={}'
                 .format(city[i], k))
    # 不用头的话，网页链接会被解析为乱码，请求失败
count = 0  # 计数器
with open('E:\MyProject\Python\JupyterNotebook/ZhiLianZhaoPin.csv', 'w', encoding='utf-8') as f:
    for url in u:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko)Chrome'}

        data = requests.get(url, headers=headers).text
        file = etree.HTML(data)
        ss = file.xpath('//*[@id="newlist_list_content_table"]/table')
        for s in ss[2:]:
            name = s.xpath('./tr[1]/td[1]/div/a/text()')[0]
            company = s.xpath('./tr[1]/td[3]/a[1]/text()')[0]
            money = s.xpath('./tr[1]/td[4]/text()')[0]
            address = s.xpath('./tr[1]/td[5]/text()')[0]
            data = s.xpath('./tr[1]/td[6]/span/text()')[0]
            fankui = s.xpath('./tr[1]/td[2]/span/text()')
            href = s.xpath('./tr[1]/td[1]/div/a/@href')[0]
            # //*[@id="newlist_list_content_table"]/table[2]/tbody/tr[1]/td[2]
            # 从2开始到61
            # 最后一页只有59行,不用考虑，不存在对应的结构
            if len(fankui) > 0:
                f.write(
                    "{},{},{},{},{},{},{}\n".format(
                        name,
                        company,
                        money,
                        address,
                        data,
                        fankui[0],
                        href))
            else:
                f.write(
                    "{},{},{},{},{},{},{}\n".format(
                        name,
                        company,
                        money,
                        address,
                        data,
                        '无',
                        href))
            count += 1
            print('正在写第{}个职位,网页是：{}\n'.format(count, url))
        time.sleep(1)
