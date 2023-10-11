# _*_coding:utf-8 _*_
# @Time　　 : 2019/8/30   16:46
# @Author　 : zimo
#@ File　   :five8pic_main.py
#@Software  :PyCharm


import requests
from fake_useragent import FakeUserAgent
import json
import time
from lxml import etree
import re
from bs4 import BeautifulSoup
ua=FakeUserAgent()
url="http://tybm.szzlb.gov.cn:10000/AddressWeb/fullquery/searchWeb.go"
headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Content-Length': '41',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'tybm.szzlb.gov.cn:10000',
            'Origin': 'http://tybm.szzlb.gov.cn:10000',
            'Referer': 'http://tybm.szzlb.gov.cn:10000/AddressWeb/fullquery/toFullQueryWeb.go',
            'User-Agent':ua.random,
            'X-Requested-With': 'XMLHttpRequest'
}
req_payload={"key": "新安街道中洲华府二期9栋D单元702", "curPage": 1}
response=requests.post(url,headers=headers,data=json.dumps(req_payload))

for i in range(3):
    if response.status_code==200 and len(response.text)>0:
        break
    else:
        time.sleep(5)
        response = requests.post(url, headers=headers, data=json.dumps(req_payload))
# print(response.text)
response_json=json.loads(response.text)
records_lst=response_json['records']
print(records_lst)

if len(records_lst)>1:
    id_lst=records_lst[1:]
else:
    id_lst=records_lst
for dic in id_lst:
    code=dic['ID']['columnVal']
    stand_addr=dic['HOUSE_STANDARD_HOUSE_FULL_ADDR']['columnVal']
    detail_addr=dic['HOUSE_DETAIL_HOUSE_FULL_ADDR']['columnVal']
    if "<span" in stand_addr:
        stand_addr_tmp="".join(etree.HTML(stand_addr).xpath("//[@class='hlShow']/text()"))
        print(detail_addr)




