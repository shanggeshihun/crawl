# _*_coding:utf-8 _*_
# @Time     :2019/8/20   0:09
# @Author   : 
# @ File　　:get_valid_ip_from_cixi.py
# @Software :PyCharm
# @Desc     :python爬虫获取大量免费有效代理ip--有效防止ip被封 https://www.kuaidaili.com/free/

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

    url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
    headers = {
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    tr_tag_list = html.xpath("//div[@class='con-body']//div[@id='list']//tbody/tr")
    for tr in tr_tag_list:
        ip = tr.xpath(r"./td[@data-title='IP']/text()")[0]
        port =tr.xpath(r"./td[@data-title='PORT']/text()")[0]
        ty = tr.xpath(r"./td[@data-title='类型']/text()")[0]
        ty_ip_port=(ty,ip,port)
        element_tuple_list.append(ty_ip_port)
    return element_tuple_list

def check_proxy(proxy_tuple_list):
    """
    :param proxy_tuple_list: （类型,IP,端口）元组组成的列表
    :return: 验证通过的proxy_dict列表
    """
    valid_proxy_dict_list=[]
    url='https://www.baidu.com/'
    for proxy_tuple in proxy_tuple_list:
        headers = {
            "Referer": "https://www.baidu.com/",
            "Sec-Fetch-Mode": "no-cors",
            "User-Agent": ua.random
        }
        ty=proxy_tuple[0].lower()
        proxy=proxy_tuple[0].lower() +'://'+proxy_tuple[1]+':'+proxy_tuple[2]
        proxy_dict={ty:proxy}
        print(proxy_dict)
        try:
            response = requests.get(url, proxies=proxy_dict,headers=headers,timeout=(3,7))
            if response.status_code==200:
                valid_proxy_dict_list.append(proxy_dict)
                print('有效IP代理:',proxy_dict)
            else:
                pass
        except Exception as e:
            print(e)
        time.sleep(1)
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