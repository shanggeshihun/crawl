# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pc6ShiwanItem(scrapy.Item):
    # define the fields for your item here like:
    href = scrapy.Field()
    program_name = scrapy.Field()
    date = scrapy.Field()
    size = scrapy.Field()
    reason = scrapy.Field()
    curr_page_url = scrapy.Field()
    author = scrapy.Field()
