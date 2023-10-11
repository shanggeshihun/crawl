# _*_coding:utf-8 _*_
# @Time　　 : 2020/8/2   21:44
# @Author　 : zimo
# @File　   :setiment_score.py
# @Software :PyCharm
# @Theme    :
from scrapy import cmdline
cmdline.execute('scrapy crawl itcast'.split())
# cmdline.execute('scrapy crawl douban_spider -o movielist.csv'.split())