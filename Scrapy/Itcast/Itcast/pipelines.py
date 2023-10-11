# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json,os
class ItcastPipeline:
    def __init__(self):
        file_path=os.path.join(os.getcwd(),'data',"itcast_pipeline.json")
        print(file_path)
        self.f=open(file_path,"w")
    def process_item(self, item, spider):
        content=json.dumps(dict(item,ensure_ascii=False))
        self.f.write(content.encode('utf-8').decode('unicode_escape'))
        # 将item返回给引擎，告诉引擎当前的item数据处理完了，可以给下一个item
        return item

    def close_spider(self,spider):
        self.f.close()
