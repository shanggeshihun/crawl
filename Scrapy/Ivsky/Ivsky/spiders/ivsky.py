import scrapy
from scrapy import Selector
from scrapy import Request
from Ivsky.items import IvskyItem

class IvskySpider(scrapy.Spider):
    name = 'ivsky'
    allowed_domains = ['www.ivsky.com']
    start_urls = ['https://www.ivsky.com/']
    # step1-爬取每个分类的地址通过回调函数传入下一层
    def parse(self, response):
        # 验证随机用户代理是否生效
        # print(response.request.headers)
        selector = Selector(response)
        # print(response.text)
        types = selector.xpath("//div[@class='kw']/a")
        for type in types:
            type_url = type.xpath("@href").extract()[0] # 分类地址
            print(type(type.xpath("text()")))
            type_name = type.xpath("text()").extract()[0] # 分类名称
            # print(typeUrl+" "+typeName)
            yield Request(self.start_urls[0] + type_url, callback=self.parse_total_page, meta={'type_name': type_name})

    # step2-进入一个类型,获取每页的链接
    def parse_total_page(self, response):
        # 验证随机用户代理是否生效
        # print(response.request.headers)
        type_name = response.meta["type_name"]
        selector = Selector(response)
        page_list = selector.xpath("//div[@class='pagelist']//a//@href").extract()  # 每一页的地址
        for page in page_list:
            yield Request(self.start_urls[0] + page, callback=self.parse_get_img, meta={'type_name': type_name})

    # step3-获取某子类某页背景图的所有地址
    def parse_get_img(self, response):
        type_name = response.meta["type_name"]
        selector = Selector(response)
        imgs = selector.xpath("//div[@class='il_img']//a")
        for img in imgs:
            img_url = img.xpath("@href").extract()[0]    # 一类图的地址
            img_name = img.xpath("@title").extract()[0]    # 一类图的地址
            yield Request(self.start_urls[0] + img_url, callback=self.parse_get_img_info, meta={'img_name': img_name})

    # step3-查看每张图片的地址
    def parse_get_img_info(self, response):
        selector = Selector(response)
        # print(response.text)
        items = IvskyItem()
        items["img_name"] = response.meta["img_name"]
        for img_url in selector.xpath("//div[@class='il_img']//a//img//@src").extract():
            items["img_url"] ='http:'+ img_url
            print(items)
            yield items