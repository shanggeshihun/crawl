# _*_coding:utf-8 _*_
# @Time     :2019/8/20   0:09
# @Author   : 
# @ File　　:test_get_valid_ip_from_cixi.py
# @Software :PyCharm
# @Desc     :python爬虫获取大量免费有效代理ip--有效防止ip被封 https://blog.csdn.net/qq_39884947/article/details/86609930

import re
import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
ua=UserAgent()

def get_all_proxy(page):
    """
    :param page: 获取第page页
    :return: （国家,IP,端口,地址,类型）元组组成的列表
    """
    url = 'http://www.xicidaili.com/nn/1'
    headers = {
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    ip_list = soup.find('table', {'id': 'ip_list'})
    td = ip_list.find_all(lambda tag: tag.name == 'tr' and tag.has_attr('class'))
    td_sub = td[0]
    element_tuple_list = []
    for td_sub in td:
        pattern = re.compile(
            r"<img\s*alt=\"(\w+)\"\s*.*?/></td>\s*<td>(.*?)</td>\s*<td>(\d+)</td>\s*<td>\s*<a\s*.*?>(.*?)</a>\s*</td>\s*<td.*?>\s*<td>(\w+)</td>")
        element_tuple = pattern.findall(str(td_sub))[0]
        element_tuple_list.append(element_tuple)
    return element_tuple_list

def check_proxy(proxy_tuple_list):
    """

    :param proxy_tuple_list: （国家,IP,端口,地址,类型）元组组成的列表
    :return: 验证通过的proxy_dict列表
    """
    valid_proxy_dict_list=[]
    url='http://www.baidu.com/'
    headers={"Referer":"https://www.baidu.com/","Sec-Fetch-Mode":"no-cors","User-Agent": ua.random}
    for proxy_tuple in proxy_tuple_list:
        ty=proxy_tuple[4].lower()
        proxy=proxy_tuple[4].lower()+'://'+proxy_tuple[1]+':'+proxy_tuple[2]
        proxy_dict={ty:proxy}
        try:
            response = requests.get(url, proxies=proxy_dict,headers=headers,timeout=5)
            if response.status_code==200:
                valid_proxy_dict_list.append(proxy_dict)
            else:
                pass
        except:
            pass
    return valid_proxy_dict_list

if __name__=='__main__':
    valid_proxy_dict_list_all=[]
    page_list=range(1,2)
    for page in page_list:
        proxy_tuple_list=get_all_proxy(page)
        valid_proxy_dict_list=check_proxy(proxy_tuple_list)
        valid_proxy_dict_list_all.extend(valid_proxy_dict_list)
    print(len(valid_proxy_dict_list_all))

[{'https': 'https://112.87.69.176:9999'},
 {'http': 'http://36.248.132.208:9999'},
 {'https': 'https://117.28.97.135:9999'},
 {'https': 'https://117.28.97.130:9999'},
 {'http': 'http://182.35.84.3:9999'},
 {'http': 'http://58.34.118.95:8118'},
 {'http': 'http://113.120.32.73:9999'},
 {'http': 'http://117.95.195.6:9999'},
 {'http': 'http://113.120.36.154:9999'},
 {'http': 'http://171.13.103.159:9999'},
 {'http': 'http://117.95.195.138:9999'},
 {'https': 'https://112.85.129.195:9999'},
 {'https': 'https://112.85.166.255:9999'},
 {'http': 'http://163.204.244.36:9999'},
 {'https': 'https://60.13.42.224:9999'},
 {'https': 'https://114.239.255.78:9999'}]
