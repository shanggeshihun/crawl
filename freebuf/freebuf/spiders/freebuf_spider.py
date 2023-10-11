# -*- coding: utf-8 -*-
import scrapy
from freebuf.items import  FreebufItem
from lxml import etree
class FreebufSpiderSpider(scrapy.Spider):
    name = 'freebuf_spider'
    allowed_domains = ['freebuf.com']
    start_urls = ['http://freebuf.com/']

    def parse(self, response):
        news_list=response.xpath('//div[@class="news_inner news-list"]')
        for news in news_list:
            # print(news.extract())
            news_item=FreebufItem()
            try:
                news_item['href']=news.xpath('.//div[@class="news-img"]/a[@target="_blank"]/@href').extract()[0]
                news_item['title']=news.xpath('.//div[@class="news-img"]/a[@target="_blank"]/img/@title').extract()[0]
                news_item['tag']=news.xpath('.//div[@class="news-img"]/a[@target="_blank"]/span/text()').extract()[0]
                news_item['autor']=news.xpath('.//div[@class="news-info"]//span/a[@rel="author"]/text()').extract()[0]
                news_item['ttime']=news.xpath('.//div[@class="news-info"]//span[@class="time"]/text()').extract()[0]
                news_item['content']=news.xpath('.//div[@class="news-info"]//dd[@class="text"]/text()').extract()[0]
                # news_item['persons']
                # news_item['if_person']
            except:
                continue
            print(len(news.extract()),news_item)
