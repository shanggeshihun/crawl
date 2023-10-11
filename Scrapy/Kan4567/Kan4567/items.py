# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Kan4567Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    detail_url = scrapy.Field()
    actor = scrapy.Field()
    bg_img_url=scrapy.Field()
