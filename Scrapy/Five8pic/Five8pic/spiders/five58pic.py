import scrapy
from Five8pic.items import Five8PicItem
class Five58picSpider(scrapy.Spider):
    name = 'five58pic'
    allowed_domains = ['58pic.com']
    start_urls = ['http://58pic.com/c']

    def parse(self, response):
        node_list = response.xpath("//div[@class='favls-wrap clearfix']/div")
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = Five8PicItem()
            # extract()将xpath对象转换为 Unicode字符串
            title = node.xpath("./a/p[@class='clearfix favls-info']/span/text()").extract()
            user_name = node.xpath("./a/p[@class='favls-info']/span[@class='info-h3 user-favor']/span[@class='usernameColor']/text()").extract()
            href = node.xpath("./a/@href").extract()
            print(title,'\n',user_name,'\n',href)

            item['title'] = title[0]
            item['user_name'] = user_name[0]
            item['href'] = href[0]

            # 返回提取到的每个item数据，等管道文件处理，同时还会回来来继续执行后面的代码
            yield item
