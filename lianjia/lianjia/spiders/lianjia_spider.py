# -*- coding: utf-8 -*-
import scrapy
import re
from collections import Counter
from lianjia.items import LianjiaItem

class LianjieSpiderSpider(scrapy.Spider):
    name = 'lianjia_spider'
    allowed_domains = ['wh.lianjia.com']
    start_urls = ['https://wh.lianjia.com/ershoufang/baibuting/']

    def parse(self, response):
        rep=response.body.decode('utf-8')
        item=LianjiaItem()
        info_list=response.xpath('//div//ul//li[@class="clear LOGCLICKDATA"]')
        print(len(info_list))
        for i in info_list:
            item["xiaoqu_name"] = i.xpath('.//div[@class="houseInfo"]//a[@target="_blank"]/text()').extract()[0]
            item["name"] = i.xpath('.//div[@class="info clear"]//a/text()').extract()[0]
            item["area"] = i.xpath('.//div[@class="info clear"]//div[@class="positionInfo"]//a/text()').extract()[0]
            item["link"] = i.xpath(".//div[@class='title']//@href").extract()[0]
            item["summary"] = i.xpath('.//div[@class="houseInfo"]/text()').extract()[0]  # summary 总结 朝向 装修等，电梯等
            item["floor"] = i.xpath('.//div[@class="info clear"]//div[@class="positionInfo"]/text()').extract()[0]
            item["zongjia"] = i.xpath('.//div[@class="info clear"]//div[@class="totalPrice"]//span/text()').extract()[
                0]  # + "万" #组合上单位
            item["danjia"] = i.xpath('.//div[@class="info clear"]//div[@class="unitPrice"]//span/text()').extract()[0]
            yield item
        area_list = ["baibuting", "dazhilu", "dijiao", "erqi2", "houhu", "huangpuyongqing"]
        for i in area_list:
            for num in range(0,2):
                yield scrapy.Request("https://wh.lianjia.com/ershoufang/"+ i +"/pg"+ str(num), callback=self.parse)


