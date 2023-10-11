import scrapy
from Wz.items import WzItem

class WzSpider(scrapy.Spider):
    name = 'wz'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/depart/index']

    def parse(self, response):
        node_list = response.xpath("//ul[@class='clear department-icon']/li")
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = WzItem()
            # extract()将xpath对象转换为 Unicode字符串
            name = node.xpath("./a/p/text()").extract()
            src = node.xpath("./a/img/@src").extract()

            item['name'] = name[0]
            item['src'] = src[0]

            # 返回提取到的每个item数据，等管道文件处理，同时还会回来来继续执行后面的代码
            yield item