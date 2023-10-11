# _*_coding:utf-8 _*_
# @Time　　 :2020/12/31   23:32
# @Author　 :
# @File　　 :ParseResponse.py
# @Theme    :单个请求页面的代理列表

from lxml import etree
import requests,json
from fake_useragent import UserAgent
import numpy as np
ua=UserAgent()

class Parse():
    def __init__(self,page):
        self.proxy_list=[]
        self.page=page
        self.run()

    def parse_yundaili(self):
        url = 'http://www.ip3366.net/free/?stype=1&page={}'.format(self.page)
        headers = {
            'User-Agent': np.random.choice(ua)
        }
        response = requests.get(url,headers=headers)
        html=etree.HTML(response.text)
        tr_tag=html.xpath('//tbody/tr')
        for tr in tr_tag:
            ty=tr.xpath('./td[4]/text()')[0].lower()
            ip=tr.xpath('./td[1]/text()')[0]
            port=tr.xpath('./td[2]/text()')[0]
            self.proxy_list.append((ty,ip,port))

    def parse_zhimadaili(self):
        url = 'http://wapi.http.linkudp.com/index/index/get_free_ip'
        headers = {
            'User-Agent': np.random.choice(ua)
        }
        data = {
            'page': self.page
        }
        response = requests.post(url, headers=headers, data=data)
        html = json.loads(response.text)['ret_data']['html']
        html = etree.HTML(html)
        tr_tag = html.xpath('//tr')
        tr_tag_name_list = tr_tag[0]
        tr_tag_list = tr_tag[1:]
        for tr in tr_tag_list:
            tmp_td_list = tr.xpath('./td')
            ip = tmp_td_list[0].xpath(r'./text()')[0]
            port = tmp_td_list[1].xpath(r'./text()')[0]
            ty = tmp_td_list[3].xpath(r'./text()')[0].lower()
            self.proxy_list.append((ty, ip, port))

    def parse_xiladaili(self):
        url = 'http://www.xiladaili.com/gaoni/{}/'.format(self.page)
        headers = {
            'User-Agent': np.random.choice(ua)
        }
        response = requests.get(url)
        html=etree.HTML(response.text)
        tr_tag=html.xpath('//tbody/tr')
        for tr in tr_tag:

            ty=tr.xpath('./td/text()')[1].lower().replace('代理','').split(',')[0]
            ip=tr.xpath('./td/text()')[0].split(':')[0]
            port=tr.xpath('./td/text()')[0].split(':')[1]
            self.proxy_list.append((ty,ip,port))

    def run(self):
        # self.parse_yundaili()
        # self.parse_zhimadaili()
        self.parse_yundaili()
if __name__ == '__main__':
    p=Parse(1)
    print(p.proxy_list)