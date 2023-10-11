# -*- coding: utf-8 -*-
import scrapy
from itcastSpider.items import ItcastspiderItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名，启动爬虫时需要的参数*必需
    name = 'itcast'
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['itcast.cn']
    # 其实是url列表，爬虫进行后第一批请求，将从这个列表里获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        node_list=response.xpath('//div[@class="maincon"]/ul/li')

        # 用来存储所有的item字段
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item=ItcastspiderItem()
            name=node.xpath('./div/h2/text()').extract()
            title=node.xpath('./div//h3/text()').extract()
            info=node.xpath('./div//p/text()').extract()

            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]

            # 返回提取到的每个item数据，给管道文件处理，同时还回来继续执行后面的代码(for 循环)
            yield  item
