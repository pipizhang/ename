import scrapy
import re
from pyquery import PyQuery
from ename.items import EnameItem

class ChaSpider(scrapy.Spider):
    name = "cha"
    base_url = "https://yingwenming.911cha.com/"
    start_urls = ["https://yingwenming.911cha.com/"]
    allowed_domains = ["yingwenming.911cha.com"]

    def parse(self, response):
        links = self.get_links(response)
        for url in links:
            yield scrapy.Request(url=url, callback=self.parse_name_page)
            #break

    def parse_name_page(self, response):
        yield self.parse_ename(response)
        #yield parse_ename(response)

        links = self.get_links(response)
        for url in links:
            #print('>> ' + url)
            yield scrapy.Request(url=url, callback=self.parse_name_page)
            #break

    def parse_ename(self, response):
        pq = PyQuery(response.body)
        data = {}

        t = pq("div.mcon p:contains('英文名')").eq(0).text()
        m = re.search(r'([a-zA-Z]+) \[(\S+)\]', t)
        if m:
            data['ename'] = m.group(1).strip()
            data['pronunciation'] = m.group(2).strip()
        else:
            return
        #print(t)

        t = pq("div.mcon p:contains('中文音译')").text()
        data['cname'] = t.replace('中文音译', '').strip()
        #print(t)

        t = pq("div.mcon p:contains('其他音译')").text()
        data['cname_ext'] = t.replace('其他音译', '').strip()
        #print(t)

        t = pq("div.mcon p:contains('名字性别')").text()
        if t.find('女孩') >= 0:
            data['gender'] = 'f'
        elif t.find('男孩') >= 0:
            data['gender'] = 'm'
        else:
            data['gender'] = 'b'
        #print(t)

        t = pq("div.mcon p:contains('来源语种')").text()
        data['origin'] = t.replace('来源语种', '').strip()
        #print(t)

        t = pq("div.mcon p:contains('名字寓意')").text()
        data['moral'] = t.replace('名字寓意', '').strip()
        #print(t)

        t = pq("div.mcon p:contains('名字印象')").text()
        data['impression'] = t.replace('名字印象', '').strip()
        #print(t)

        t = pq("div.mcon p:contains('名字含义')").text()
        data['meaning'] = t.replace('名字含义', '').strip()
        #print(t)

        t = pq("div.mcon p:contains('相似英文名')").text()
        data['similar'] = t.replace('相似英文名', '').strip()
        #print(t)

        for k, v in data.items():
            if v == "暂无":
                data[k] = ""

        return EnameItem(**data)

    def get_links(self, response):
        links = response.xpath('//a/@href').getall()
        urls = []
        for url in links:
            if re.match('^\.\/[A-Z]+[a-z]+\.html', url):
                url = '{}{}'.format(self.base_url, url[2:])
                urls.append(url)
        return urls

