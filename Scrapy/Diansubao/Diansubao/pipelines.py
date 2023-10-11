# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv,os
class DiansubaoPipeline:
    def __init__(self):
        self.f = open(os.path.join(os.getcwd(), 'data', "diansubao.csv"), mode="a", encoding='utf-8', newline="")
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.fieldnames = ["age","article_link","back_time","category","cdate","company_id","company_name","company_web","concrete_area","ctime","email","id","idcard","intro","manager","mobile","money","name","order_num","pic1","pic1_info","pic2","pic2_info","pic3","pic3_info","pic4","pic4_info","pic5","pic5_info","post_time","remark","remark2","review","sex","state","time1","time2","time3","title","to_company"]
        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 写入spider传过来的具体数值
        self.writer.writerow(item)
        print(item)
        # 写入完返回
        return item

    def close(self, spider):
        self.f.close()
