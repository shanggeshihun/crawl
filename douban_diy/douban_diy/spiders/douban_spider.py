# -*- coding: utf-8 -*-
import scrapy
from douban_diy.items import DoubanDiyItem
from bs4 import BeautifulSoup
import re
class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        soup=BeautifulSoup(response.text,'lxml')
        li_lst=soup.find('ol',{'class':'grid_view'}).find_all('li')
        for li in li_lst:
            douban_diy_item=DoubanDiyItem()
            douban_diy_item['serial_number']=li.find('div',{'class':'pic'}).get_text().strip()
            douban_diy_item['movie_name']=li.find('div',{'class':'hd'}).get_text().split()[0]
            # douban_diy_item['describle']=li.find('p',{'class':'quote'}).get_text().strip()
            douban_diy_item['star']=li.find('span',{'class':'rating_num','property':'v:average'}).get_text()
            douban_diy_item['evaluate']=re.findall(r'<span>(\d+人评价)</span>',str(li))[0]
            yield douban_diy_item
        next_link=re.findall(r'<link\s+rel=\"next\"\s+href=\"(.*?)\"/>',response.text)
        if next_link:
            next_link=next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)
