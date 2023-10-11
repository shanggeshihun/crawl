import scrapy
from Itcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list=response.xpath("//div[@class='maincon']/ul[@class='clears']/li")
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item=ItcastItem()
            # extract()将xpath对象转换为 Unicode字符串
            name=node.xpath("./div[@class='main_bot']/h2/text()").extract()
            title=node.xpath("./div[@class='main_bot']/h2/span/text()").extract()
            info=node.xpath("./div[@class='main_mask']/p/text()").extract()
            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]

            # 返回提取到的每个item数据，等管道文件处理，同时还会回来来继续执行后面的代码
            yield item

