# _*_coding:utf-8 _*_

#@Time      : 2021/12/15  14:43
#@Author    : An
#@File      : gametrademain.py
#@Software  : PyCharm

from scrapy import cmdline
cmdline.execute('scrapy crawl trader_list'.split())
