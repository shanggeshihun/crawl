# -*- coding: utf-8 -*-
import scrapy
import time

class RenrenSpiderSpider(scrapy.Spider):
    name = 'renren_spider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        base_url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp='
        s=time.strftime('%S')
        ms=int(round(time.time()%(int(time.time())),3)*1000)
        date_time='20198223'+str(s)+str(ms)
        login_url=base_url+date_time
        data={'email':'1569873132@qq.com',
              'icode':'',
              'origURL':'http://www.renren.com/home',
              'domain':'renren.com',
              'key_id':'1',####注意这里面一定是字符型1，整型1会报错。如果使用
###request.session（）应该没有这个问题
              'captcha_type':'web_login',
              'password':'2c52d520cd3e66994f1815509775cdd65a157f3cf22305ace2d8fe1970927769',
              'rkey':'2e8b9e448f19a74b67a18616eced35c0',
              'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DF2pYkLiJ_pEabeL8zGf36hQNg2LqMakrL_Y4TLSk0aa%26wd%3D%26eqid%3D9580ad4d003de4cc000000065d653c45'}
        yield scrapy.FormRequest(url=login_url, formdata=data, callback=self.parse_login, dont_filter=True)

    def parse_login(self, response):
            yield scrapy.Request(url='http://www.renren.com/487881229/profile', callback=self.parse_text,
                                 dont_filter=True)
    def parse_text(self, response):
        with open(r'E:\大鹏.html', 'w', encoding='utf-8') as f:
            f.write(response.text)