# _*_coding:utf-8 _*_
# @Time     :2019/8/20   1:31
# @Author   : 
# @ File　　:test_proxy_list_if_valid.py
# @Software :PyCharm
# @Desc     :http://www.data5u.com/ 测试高匿IP
import re
import requests
from bs4 import BeautifulSoup
import time

from get_proxy_lst import get_proxy_lst

def check_proxy(proxy):
    """
    :param proxy代理
    :return: 返回bool
    """
    import json
    url='http://httpbin.org/ip'
    # url='http://h.zhimaruanjian.com/'
    flag=True
    try:
        response = requests.get(url, proxies=proxy,timeout=(3,7))
        if response.status_code==200:
            response_dict=json.loads(response.text)
            print(proxy,response_dict['origin'])
        else:
            flag=False
    except:
        flag=False
    return flag
if __name__=='__main__':
    valid_proxy_dict_list=[]
    proxy_dict_list=get_proxy_lst()
    for proxy in proxy_dict_list:
        f=check_proxy(proxy)
        if f:
            valid_proxy_dict_list.append(proxy)
    print('测试可用IP池列表：\n',valid_proxy_dict_list)