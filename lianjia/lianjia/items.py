# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xiaoqu_name=scrapy.Field()
    name=scrapy.Field()
    area=scrapy.Field()
    link=scrapy.Field()
    summary=scrapy.Field()
    floor=scrapy.Field()
    zongjia=scrapy.Field()
    danjia=scrapy.Field()
