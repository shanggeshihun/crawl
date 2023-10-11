# _*_coding:utf-8 _*_
# @Time     :2019/8/20   0:09
# @Author   : 
# @ File　　:get_valid_ip_from_cixi.py
# @Software :PyCharm
# @Desc     :python爬虫获取大量免费有效代理ip--有效防止ip被封 http://h.zhimaruanjian.com/?utm-source=bdtg&utm-keyword=?6077

import re,json
import requests
from lxml import etree
import time
from fake_useragent import UserAgent
ua=UserAgent()

def get_all_proxy(page):
    """
    :param page: 获取第page页
    :return: （类型,IP,端口）元组组成的列表
    """
    element_tuple_list = []

    url = 'http://wapi.http.linkudp.com/index/index/get_free_ip'
    headers = {
        'User-Agent': ua.random
    }
    data={
        'page':page
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
        ty = tmp_td_list[3].xpath(r'./text()')[0]
        ty_ip_port=(ty,ip,port)
        element_tuple_list.append(ty_ip_port)
    return element_tuple_list

def check_proxy(proxy_tuple_list):
    """
    :param proxy_tuple_list: （类型,IP,端口）元组组成的列表
    :return: 验证通过的proxy_dict列表
    """
    valid_proxy_dict_list=[]
    url='http://h.zhimaruanjian.com/'
    for proxy_tuple in proxy_tuple_list:
        headers = {"Referer": "http://h.zhimaruanjian.com/",  "User-Agent": ua.random}
        ty=proxy_tuple[0].lower()
        proxy=proxy_tuple[0].lower() +'://'+proxy_tuple[1]+':'+proxy_tuple[2]
        proxy_dict={ty:proxy}
        try:
            response = requests.get(url, proxies=proxy_dict,headers=headers,timeout=(3,7))
            if response.status_code==200:
                valid_proxy_dict_list.append(proxy_dict)
                print('有效IP代理:',proxy_dict)
            else:
                pass
        except:
            pass
    return valid_proxy_dict_list

if __name__=='__main__':
    valid_proxy_dict_list_all=[]
    page_list=range(1,5)
    for page in page_list:
        proxy_tuple_list=get_all_proxy(page)
        print(proxy_tuple_list)
        valid_proxy_dict_list=check_proxy(proxy_tuple_list)
        valid_proxy_dict_list_all.extend(valid_proxy_dict_list)
    print(len(valid_proxy_dict_list_all))