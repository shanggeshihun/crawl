# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItcastspiderPipeline(object):
    def __init__(self):
        self.f=open('itcast_pipeline.json','w')
        pass

    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)
        self.f.write(content)
        # 告诉引擎item处理完了，可以继续给下一个item
        return item

    def close_spieder(self,spider):
        self.f.close()

