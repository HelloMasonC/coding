# -*- coding: utf-8 -*-
import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    data_list = []

    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "root123456."
        database = "dangdang"
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
        self.cur = self.conn.cursor()
    
    def open_spider(self, spider):
       # 如果连接数据库失败会自动重新链接
        try:
            host = "127.0.0.1"
            user = "root"
            password = "root123456."
            database = "dangdang"
            self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
            self.cur = self.conn.cursor()
        except:
            self.open_spider()
        else:
            spider.logger.info('MySQL: connected')

            self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
            spider.cur = self.cur

    def insert_data(self, data):
       # 这个函数是用来往数据库中写入数据的。
       # 传过来的data是一个元祖，经尝试字典是不可以的，也就是说我们不可以直接把item传给这个函数。
        print('begin insert data')
        try:
            sql = 'INSERT INTO books(title, link, cost, bookshop, comment) VALUES(%s, %s, %s, %s, %s)'
            self.cur.executemany(sql, data)
            self.conn.commit()
            print("success insert 5 data")
        except:
            self.conn.rollback()
            print('insert warnning')

    def process_item(self, item, spider):
        for i in range(0, len(item['title'])):
            if len(self.data_list) == 1000:
            # 这里是判断你一次性要插入多少条数据可自行修改
                self.insert_data(self.data_list)
                self.data_list = []
            else:
                self.data_list.append((item['title'][i], item['link'][i], item['cost'][i], item['bookshop'][i], item['comment'][i]))
        return item

    def close_spider(self, spider):
        self.insert_data(self.data_list)
        self.conn.commit()
        self.cur.close()
        self.conn.close()