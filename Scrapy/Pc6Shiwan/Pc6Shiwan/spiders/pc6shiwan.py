import scrapy,time
from lxml import  etree
from Pc6Shiwan.items import Pc6ShiwanItem

class Pc6shiwanSpider(scrapy.Spider):
    name = 'pc6shiwan'
    allowed_domains = ['www.pc6.com']
    start_urls = ['http://www.pc6.com/pc/shiwanzhuanqapp/1/']

    def parse(self, response):
        html=etree.HTML(response.text)
        li=html.xpath(r"//ul[@class='clearfix mainCont']/li")
        cur_page=int(html.xpath(r"//div[@class='page']/@data-page")[0])
        print('cur_page',cur_page)
        for line in li:
            href = line.xpath(r"./p/s/a/@href")[0]
            program_name = line.xpath(r"./p/a/strong/text()")[0]
            date = line.xpath(r"./p/text()")[0].split('/')[0]
            size = line.xpath(r"./p/text()")[0].split('/')[1]
            reason = line.xpath(r"./p/em/strong/text()")[0]
            curr_page_url = 'http://www.pc6.com/pc/shiwanzhuanqapp/{}/'.format(cur_page)
            yield scrapy.Request(href,callback=self.parse_info,meta={'href':href,'program_name':program_name,'date':date,'size':size,'reason':reason,'curr_page_url':curr_page_url})

        try:
            next_link_flag = html.xpath(r"//span[@class='next_link']/text()")[0]
            print('next_link_flag',next_link_flag)
        except Exception as e:
            next_link_flag=False
        if not next_link_flag:
            next_url_page=cur_page+1
            next_url='http://www.pc6.com/pc/shiwanzhuanqapp/{}/'.format(next_url_page)
            print('next_url', next_url)
            time.sleep(1)
            yield  scrapy.Request(url=next_url,callback=self.parse)

    def parse_info(self,response):
        html=etree.HTML(response.text)
        try:
            author=html.xpath(r"//p[@class='base']/i[@class='system']/s/@title")[0]
        except:
            author='暂无'
        item = Pc6ShiwanItem()
        item['href']=response.meta['href']
        item['program_name']=response.meta['program_name']
        item['date']=response.meta['date']
        item['size']=response.meta['size']
        item['reason']=response.meta['reason']
        item['curr_page_url']=response.meta['curr_page_url']
        item['author']=author
        yield  item


