# _*_coding:utf-8 _*_
# @Time　　 :2020/12/31   22:44
# @Author　 :
# @File　　 :proxy_main.py
# @Theme    :PyCharm

import threading,requests,json,time
from fake_useragent import UserAgent
from queue import Queue
import numpy as np
from lxml import etree
import os,time
from ParseResponse import Parse

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
                p=Parse(page)
                proxy_list=p.proxy_list
                for p in proxy_list:
                    self.proxy_queue.put({p[0]: p[0] + "://" + p[1] + ":" + p[2]})
                    print('IpThread',{p[0]: p[0] + "://" + p[1] + ":" + p[2]})
            except:
                pass
            time.sleep(1)

class VerifyIpThread(threading.Thread):
    def __init__(self,thread_id,proxy_queue,file_path):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.proxy_queue=proxy_queue
        self.file_path=file_path

    def run(self):
        while PROXY_QUEUE_FLAG:
            if  self.proxy_queue.empty():
                break
            proxy=self.proxy_queue.get()
            test_ip = json.dumps(proxy).split('//')[1].split(':')[0].strip()
            try:
                res = requests.get('http://httpbin.org/ip', proxies=proxy, timeout=(3, 27))
            except Exception as e:
                pass
                # print('VerifyIpThread:',e)
            else:
                res_to_json = json.loads(res.text)
                result_ip = res_to_json['origin'].strip()
                print(proxy,'test_ip:',test_ip,'result_ip',result_ip)
                if test_ip == result_ip:
                    with open(self.file_path,'a+') as f:
                        f.write(str(proxy))
                        f.write('\n')
                    print('有效代理:', proxy)

PAGE_QUEUE_FLAG=True
PROXY_QUEUE_FLAG=True

def main():
    page_queue=Queue()
    proxy_queue=Queue()


    for page in range(1,10):
        page_queue.put(page)

    ip_thread_list=[]
    for i in range(3):
        ip_thread = IpThread(i, page_queue,proxy_queue)
        ip_thread.start()
        ip_thread_list.append(ip_thread)
    # 等待待爬取的页面已经全面遍历完
    while not page_queue.empty():
        pass
    global PAGE_QUEUE_FLAG
    PAGE_QUEUE_FLAG=False
    for t in ip_thread_list:
        t.join()

    verify_thread_list=[]
    for i in range(10):
        verify_thread = VerifyIpThread(i, proxy_queue,file_path=os.path.join(os.getcwd(),'valid_proxy.txt'))
        verify_thread.start()
        verify_thread_list.append(verify_thread)
    # 等待验证页面已经全面遍历完
    while not proxy_queue.empty():
        pass
    global PROXY_QUEUE_FLAG
    PROXY_QUEUE_FLAG=False
    for t in verify_thread_list:
        t.join()
    print('final')

if __name__ == '__main__':
    main()
