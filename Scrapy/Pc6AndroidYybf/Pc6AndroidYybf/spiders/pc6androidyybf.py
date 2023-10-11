import scrapy
from scrapy import Selector
from Pc6AndroidYybf.items import Pc6AndroidyybfItem

class Pc7androidyybfSpider(scrapy.Spider):
    name = 'pc6androidyybf'
    allowed_domains = ['www.pc6.com']
    # 该页面 爬站起始页面，通过next页翻页
    start_urls = ['http://www.pc6.com/android/584_1.html']

    # step1-解析该页面下所有的应用，并获取下一页面的链接
    def parse(self, response):
        selector = Selector(response)
        cur_url=response.url
        p = selector.xpath("//dl[@id='listCont']/dd/p")
        for p_tmp in p:
            name = p_tmp.xpath("./a/i/text()").extract_first() # 应用名称
            date=p_tmp.xpath("./font/text()").extract_first()  # 应用日期
            info_url=p_tmp.xpath("./a[@target='_blank']/@href").extract_first() # 应用详情链接
            download_url=p_tmp.xpath("./a[@class='btn']/@href").extract_first() # 应用下载链接
            yield scrapy.Request('http://www.pc6.com' + info_url, callback=self.parse_info, meta={'name': name,'cur_url':cur_url,'date':date,'download_url':'http://www.pc6.com'+ download_url})

         # 提取下一页的url
        next_url=selector.xpath("//div[@class='tsp_nav']/a[@class='tsp_next']/@href").extract_first()
        if next_url:
            yield scrapy.Request(url='http://www.pc6.com' + next_url, callback=self.parse)


    # step2-解析应用详情
    def parse_info(self,response):
        selector=Selector(response)
        items=Pc6AndroidyybfItem()
        items['name']=response.meta['name']
        items['cur_url']=response.meta['cur_url']
        items['date']=response.meta['date']
        items['download_url']=response.meta['download_url']
        items['intro']=''.join(selector.xpath(r"//dd[@id ='soft-info']/div/p[1]/text()").extract()).replace(' ','')
        yield items
