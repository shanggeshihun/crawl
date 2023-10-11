# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pc6AndroidyybfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    cur_url=scrapy.Field()
    intro = scrapy.Field()
    date=scrapy.Field()
    download_url = scrapy.Field()



