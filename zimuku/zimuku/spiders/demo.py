# -*- coding: utf-8 -*-
import scrapy

#scrapy startproject zimuku
#scrapy genspider demo  http://zimuku.net
#运行爬虫 scrapy crawl demo
# from zimuku.items import ZimukuItem
from zimuku.items import ZimukuItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.net']


    start_urls = []
    for i in range(1, 51):
        start_urls.append('http://zimuku.net/newsubs?p=' + str(i) + '/')

    def parse(self, response):
        '''
        parse()函数接收Response参数，就是网页爬取后返回的数据用于处理响应，他负责解析爬取的内容
        生成解析结果的字典，并返回新的需要爬取的请求
        '''
        #只取出第一个字幕的名字
        #xpath规则可以通过查看网页源文件得出
        # name = response.xpath('//b/text()').extract()
        #建立一个items字典，用于保存我们爬到的结果，并返回给pipline处理
        items = []
        # i=0
        # for val in name:
        #     items[i]= name[i].strip()
        #     i += 1
        #     print('index：',i)
        ret = response.xpath('//td[@class="first"]/a').extract()
        # print('ret：', ret)
        #
        for info in ret:
            item = ZimukuItem()
            print('info：', info)
            item['href'] = info.xpath('a/@href').extract()
            item['title'] = info.xpath('a/@title').extract()
            print('href：', item['href'],item['title'])

            # item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
            # item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
            # item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
            # item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # items.append(item)

        return items
