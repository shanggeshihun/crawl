# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib.request import urlretrieve
import os

def Schedule(blocknum,blocksize,totalsize):
     '''''
     blocknum:已经下载的数据块
     blocksize:数据块的大小
     totalsize:远程文件的大小
     '''
     per = 100.0 * blocknum * blocksize / totalsize
     if per > 100 :
         per = 100
     print('当前下载进度：%d'% per)


class Kan4567Pipeline:
    def process_item(self, item, spider):
        urlretrieve(item['bg_img_url'], os.path.join(os.getcwd(), 'save_files', item['bg_img_url'].split('/')[-1]),Schedule)
        return item

# class IvskyPipeline: #     def process_item(self, item, spider): #         print('--------------------------',item['bg_img_url'].split('/')[-1]) #         urlretrieve(item['bg_img_url'],os.path.join(os.getcwd(),'save_files',item['bg_img_url'].split('/')[-1])) #         return item