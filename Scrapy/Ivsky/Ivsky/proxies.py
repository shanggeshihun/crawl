# _*_coding:utf-8 _*_
# @Time　　 :2020/12/30   20:42
# @Author　 :
# @File　　 :proxies.py
# @Theme    :PyCharm
import requests
from lxml import etree
from threading import Thread
import random,json,time
from queue import Queue
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)   Chrome/45.0.2454.101 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
def get_proxies(page_stop):
    proxies=[]
    page = 1
    while page < page_stop:

        url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        print(page, page_stop,url)
        response = requests.get(url, headers=headers)
        html = etree.HTML(response.text)
        tr_tag_list = html.xpath("//div[@class='con-body']//div[@id='list']//tbody/tr")
        for tr in tr_tag_list:
            ip = tr.xpath(r"./td[@data-title='IP']/text()")[0]
            port = tr.xpath(r"./td[@data-title='PORT']/text()")[0]
            ty = tr.xpath(r"./td[@data-title='类型']/text()")[0]

            protocol =ty.lower()+'://'+ip+':'+port
            print('page:',page,':',protocol)
            proxies.append(protocol)
    return proxies


def verify_proxy(proxies_list):
    verify_proxies_list=[]
    for proxy in proxies_list:
        protocol = 'https' if 'https' in proxy else 'http'
        proxies = {protocol: proxy}
        try:
            if requests.get('https://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
                print ('success %s' % proxy)
                verify_proxies_list.append(proxies)
        except:
            pass
    return verify_proxies_list


if __name__ == '__main__':
    proxies=get_proxies(3)
    verify_proxies_list=verify_proxy(proxies)
    with open(r'D:\learn\software_learn\NOTE\Python\Scrapy\Ivsky\Ivsky\proxies.txt', 'a') as f:
        for proxy in verify_proxies_list:
             f.write(str(proxy)+'\n')