# _*_coding:utf-8 _*_
# @Time　　 : 2019/8/29   9:41
# @Author　 : zimo
#@ File　   :five8pic_main.py
#@Software  :PyCharm

from scrapy import cmdline
cmdline.execute('scrapy crawl freebuf_spider'.split())

"""
import requests
from lxml import etree
url="http://www.freebuf.com"
headers={
"Host": "www.freebuf.com",
"Pragma": "no-cache",
"Referer": "https://www.freebuf.com/",
"Sec-Fetch-Site": "same-origin",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"
}
response=requests.get(url,headers=headers).text
html=etree.HTML(response)
item_list=html.xpath('//div[@class="news_inner news-list"]')
print(etree.tostring(item_list[0]))
"""