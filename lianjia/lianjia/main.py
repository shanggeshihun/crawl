# _*_coding:utf-8 _*_
# @Time　　 : 2019/8/28   16:42
# @Author　 : zimo
#@ File　   :five8pic_main.py
#@Software  :info_list 有问题
# from scrapy import cmdline
# cmdline.execute('scrapy crawl lianjia_spider'.split())

from lxml import etree
from fake_useragent import FakeUserAgent
ua=FakeUserAgent()
headers={
    "Content-Type":"application/json",
    "Server":"Lianjia",
    "User-Agent":ua.random
}
import requests
url=r"https://wh.lianjia.com/ershoufang/baibuting/"
response=requests.get(url,headers=headers).text
res=etree.HTML(response)
result=res.xpath('//div//ul//li[@class="clear LOGCLICKDATA"]')
print(result)
