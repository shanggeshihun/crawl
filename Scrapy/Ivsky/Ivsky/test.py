# _*_coding:utf-8 _*_
# @Time　　 :2020/12/31/031   12:55
# @Author　 : Antipa
# @File　　 :get_webgame_info.py
# @Theme    :PyCharm
# import requests,json
# import numpy as np
# proxies_list=[
#     {'http': 'http://60.168.206.120:8397'}, {'https': 'https://115.221.241.120:8884'}, {'http': 'http://175.42.158.112:9009'}, {'https': 'https://113.194.28.61:8415'}, {'http': 'http://60.167.103.150:8208'}, {'http': 'http://117.64.237.247:8604'}, {'https': 'https://123.55.106.21:8161'}, {'https': 'https://183.166.103.29:8558'}, {'http': 'http://27.192.174.91:8701'}, {'http': 'http://27.206.76.28:8338'}, {'http': 'http://42.238.91.46:9009'}, {'http': 'http://175.44.108.71:9021'}, {'http': 'http://115.218.3.214:8981'}, {'https': 'https://175.43.156.39:8094'}, {'http': 'http://27.220.120.130:8499'}, {'http': 'http://27.10.163.159:8937'}, {'https': 'https://115.221.243.81:8666'}, {'http': 'http://163.125.19.214:8665'}, {'http': 'http://175.42.158.31:8216'}, {'http': 'http://58.220.95.44:8693'}]
#
# url='http://httpbin.org/ip'

# for proxy in proxies_list:
#     test_ip=json.dumps(proxy).split('//')[1].split(':')[0].strip()
#     try:
#         res=requests.get('http://httpbin.org/ip',proxies=proxy,timeout=(3,7))
#     except Exception as e:
#         pass
#     else:
#         res_to_json=json.loads(res.text)
#         result_ip=res_to_json['origin'].strip()
#         if test_ip==result_ip:
#             print('有效代理:',proxy)

import threading,requests,json,time
from fake_useragent import UserAgent
from queue import Queue
import numpy as np
from lxml import etree

ua=UserAgent()

class IpThread(threading.Thread):
    def __init__(self,thread_id,page_queue,proxy_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.page_queue=page_queue
        self.proxy_queue=proxy_queue

    def run(self):
        while  PAGE_QUEUE_FLAG:
            if  self.page_queue.empty():
                break
            page=self.page_queue.get()
            try:
                url = 'http://wapi.http.linkudp.com/index/index/get_free_ip'
                headers = {
                    'User-Agent': np.random.choice(ua)
                }
                data = {
                    'page': page
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
                    self.proxy_queue.put({ty.lower(): ty.lower() + "://" + ip + ":" + port})
                    print('IpThread',{ty.lower(): ty.lower() + "://" + ip + ":" + port})
            except:
                pass
            time.sleep(1)

class VerifyIpThread(threading.Thread):
    def __init__(self,thread_id,proxy_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.proxy_queue=proxy_queue

    def run(self):
        print(self.proxy_queue.empty())
        while PROXY_QUEUE_FLAG:
            if  self.proxy_queue.empty():
                break
            proxy=self.proxy_queue.get()
            print('VerifyIpThread:',proxy)
            test_ip = json.dumps(proxy).split('//')[1].split(':')[0].strip()
            try:
                res = requests.get('http://httpbin.org/ip', proxies=proxy, timeout=(3, 7))
            except Exception as e:
                print('VerifyIpThread:',e)
                pass
            else:
                res_to_json = json.loads(res.text)
                result_ip = res_to_json['origin'].strip()
                print('test_ip:',test_ip,'result_ip',result_ip)
                if test_ip == result_ip:
                    print('有效代理:', proxy)

PAGE_QUEUE_FLAG=True
PROXY_QUEUE_FLAG=True

def main():
    page_queue=Queue()
    proxy_queue=Queue()


    for page in range(1,3):
        page_queue.put(page)

    # 等待待爬取的页面已经全面遍历完
    while not page_queue.empty():
        pass
    ip_thread_list=[]
    for i in range(3):
        ip_thread = IpThread(i, page_queue,proxy_queue)
        ip_thread.start()
        ip_thread_list.append(ip_thread)

    verify_thread_list=[]
    for i in range(3):
        print(i)
        verify_thread = VerifyIpThread(i, proxy_queue)
        verify_thread.start()
        verify_thread_list.append(verify_thread)

    for t in ip_thread_list:
        t.join()

    for t in verify_thread_list:
        t.join()

    print('final')

if __name__ == '__main__':
    main()
