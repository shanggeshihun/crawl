# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import openpyxl,os

class Pc6AndroidyybfPipeline:
    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.ws=self.wb.active
        self.ws.append(['name','date','download_url','intro'])
        self.filepath=os.path.join(os.getcwd(),'data','result.xlsx')

    def process_item(self, item, spider):
        line=[item['name'],item['date'],item['download_url'],item['intro']]
        self.ws.append(line)
        return item

    def close_spider(self,spider):
        self.wb.save(self.filepath)


from twisted.enterprise import adbapi
import datetime
class Pc6AndroidyybfMysqlPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        # 从项目的配置文件中读取相应的参数
        # cls.MYSQL_DB_NAME = crawler.settings.get("MYSQL_DB_NAME")
        cls.HOST = crawler.settings.get("MYSQL_HOST")
        cls.PORT = crawler.settings.get("MYSQL_PORT")
        cls.USER = crawler.settings.get("MYSQL_USER")
        cls.PASSWD = crawler.settings.get("MYSQL_PASSWORD")
        return cls()

    def open_spider(self, spider):
        self.dbpool = adbapi.ConnectionPool('pymysql', host=self.HOST, port=self.PORT, user=self.USER,
                                            passwd=self.PASSWD, charset='utf8')

    def process_item(self, item, spider):
        # 提交
        query=self.dbpool.runInteraction(self.insert_db, item)
        query.addErrback(self.handle_error)  # 处理异常
        return item

    def handle_error(self, failure):
        # 处理异步插入时的异常
        print(failure)

    def close_spider(self, spider):
        # 关闭连接
        self.dbpool.close()

    def insert_db(self, cur, item):
        # 取出数据，执行cur sql
        create_date = datetime.datetime.now().date()
        create_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        values = (
            item['name'],
            item['date'],
            item['download_url'],
            item['intro']
        )
        sql = 'insert into test_new.pc6_yybo_t(name,date,download_url,intro) values (%s' + ',%s' * 3 + ')'
        cur.execute(sql, values)
