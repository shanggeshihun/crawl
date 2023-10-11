import scrapy
from lxml import etree
import json
from Diansubao.items import DiansubaoItem

class DiansubaoSpider(scrapy.Spider):
    name = 'diansubao'
    ## http://www.315.100ec.cn会自动太转到http://www.100ec.cn
    # allowed_domains = ['http://www.315.100ec.cn']
    start_urls = ['http://www.315.100ec.cn/api/index.php?_a=product&f=complain&page_record=1000&state=&p=1']

    def parse(self, response):
        res_to_json=json.loads(response.text)
        curr_page=int(res_to_json['curr_page'])
        page_total=res_to_json['page_total']
        # page_total=2
        pw_rec_list=res_to_json['pw_rec_list']
        # print(response.request.headers)
        for line in pw_rec_list:
            item=DiansubaoItem()
            item['age'] = line['age']
            item['article_link'] = line['article_link']
            item['back_time'] = line['back_time']
            item['category'] = line['category']
            item['cdate'] = line['cdate']
            item['company_id'] = line['company_id']
            item['company_name'] = line['company_name']
            item['company_web'] = line['company_web']
            item['concrete_area'] = line['concrete_area']
            item['ctime'] = line['ctime']
            item['email'] = line['email']
            item['id'] = line['id']
            item['idcard'] = line['idcard']
            item['intro'] = line['intro']
            item['manager'] = line['manager']
            item['mobile'] = line['mobile']
            item['money'] = line['money']
            item['name'] = line['name']
            item['order_num'] = line['order_num']
            item['pic1'] = line['pic1']
            item['pic1_info'] = line['pic1_info']
            item['pic2'] = line['pic2']
            item['pic2_info'] = line['pic2_info']
            item['pic3'] = line['pic3']
            item['pic3_info'] = line['pic3_info']
            item['pic4'] = line['pic4']
            item['pic4_info'] = line['pic4_info']
            item['pic5'] = line['pic5']
            item['pic5_info'] = line['pic5_info']
            item['post_time'] = line['post_time']
            item['remark'] = line['remark']
            item['remark2'] = line['remark2']
            item['review'] = line['review']
            item['sex'] = line['sex']
            item['state'] = line['state']
            item['time1'] = line['time1']
            item['time2'] = line['time2']
            item['time3'] = line['time3']
            item['title'] = line['title']
            item['to_company'] = line['to_company']
            yield item

        if curr_page<=page_total:
            print('curr_page:',curr_page,'_',page_total)
            next_url='http://www.315.100ec.cn/api/index.php?_a=product&f=complain&page_record=1000&state=&p={}'.format(curr_page+1)
            yield  scrapy.Request(url=next_url,callback=self.parse)
