# _*_coding:utf-8 _*_
# @Time　　 : 2019/8/24   17:59
# @Author　 : zimo
#@ File　   :five8pic_main.py
#@Software  :PyCharm
from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider'.split())

"""
import requests
import re
response=requests.get(r"https://movie.douban.com/top250")
next_line=re.findall(r'<link\s+rel=\"next\"\s+href=\"(.*?)\"/>',response.text)
print(next_line)
"""

import nltk