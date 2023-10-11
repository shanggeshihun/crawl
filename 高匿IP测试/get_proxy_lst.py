# # _*_coding:utf-8 _*_
# # @Time　　 : 2020/1/5   22:59
# # @Author　 : zimo
# # @File　   :qcc_qy_info.py
# # @Software :PyCharm
# # @Theme    :获取高匿IP列表，该网站获取的port已加密


from get_user_agent import *
import requests
from lxml import etree

def get_proxy_lst():
    user_agent=get_user_agent()
    proxy_lst=[]
    url='http://www.data5u.com/'
    headers={
        "Accept-Encoding":"gzip, deflate",
        "User-Agent":user_agent
    }
    res=requests.get(url,headers=headers)
    # res.encoding='utf-8'
    html=etree.HTML(res.text)
    proxy_info=html.xpath('//li[@style="text-align:center;"]/ul[@class]')
    for p in proxy_info[1:]:
        http=p.xpath('./span/li/text()')[3]
        ip=p.xpath('./span/li/text()')[0]
        port=p.xpath('./span/li/text()')[1]
        tmp_lst={http:http+"://"+ip+":"+port}
        proxy_lst.append(tmp_lst)
    print(proxy_lst)
    return proxy_lst

if __name__ == '__main__':
    proxy_lst=get_proxy_lst()
    print(proxy_lst)