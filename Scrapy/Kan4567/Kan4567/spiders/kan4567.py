import scrapy
from Kan4567.items import Kan4567Item

class Kan4567Spider(scrapy.Spider):
    name = 'kan4567'
    allowed_domains = ['www.4567kan.com']
    start_urls = ['http://www.4567kan.com/frim/index1.html']

    page = 1
    page_url = "http://www.4567kan.com/frim/index1-%s.html"

    def parse(self, response):
        print('response_url',response.url)
        li_list = response.xpath('//li[@class="col-md-6 col-sm-4 col-xs-3"]')
        for li in li_list:
            # 电影名称
            name = li.xpath('./div/a/@title').extract_first()
            # 电影背景图片链接
            bg_img_url=li.xpath('./div/a/@data-original').extract_first()
            # 电影详细链接
            detail_url = 'http://www.4567kan.com' + li.xpath('./div/a/@href').extract_first()

            # meta参数:请求传参.meta字典就会传递给回调函数的response参数
            # 在解析过程中产生新的url，需要对新的url再次发起请求时，yield 手动调用scrapy.Request方法对象，
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'name':name,'bg_img_url':bg_img_url,'detail_url':detail_url},dont_filter=True)

        # 获取前三页的数据
        print(self.page)
        if self.page <=6:
            self.page += 1
            new_page_url = self.page_url % self.page
            yield scrapy.Request(url=new_page_url, callback=self.parse,dont_filter=True)

    # 解析详情页中的数据
    def parse_detail(self, response):
        item = Kan4567Item()  # 实例化item对象
        # response.meta返回接收到的meta字典
        item['name'] = response.meta['name']
        item['detail_url'] = response.meta['detail_url']
        item['bg_img_url']=response.meta['bg_img_url']
        # 从电影详情页获取导演
        actor = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[3]/a/text()').extract_first()
        item['actor'] = actor

        print(item)
        yield item
