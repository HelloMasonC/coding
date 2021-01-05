# -*- coding: utf-8 -*-
import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", password="root123456.", db="dangdang")
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            cost = item['cost'][i]
            bookshop = item['bookshop'][i]
            comment = item['comment'][i]
            print(title + "\n" + link + "\n" + cost + "\n" + bookshop + "\n" + comment + "\n")
            sql = 'INSERT INTO books(title, link, cost, bookshop, comment) VALUES(%s, %s, %s, %s, %s)'
            param = (title, link, cost, bookshop, comment)
            try:
                cursor = conn.cursor()
                cursor.execute(sql, param)
                conn.commit()
                print("插入成功！")
            except Exception as e:
                print(e)
                conn.rollback()
            # try:
            #     with conn.cursor() as cursor:
            #         cursor.execute(sql, param)
            #     conn.commit()
            #     print("插入成功！")
            # except Exception as e:
            #     print(e)
            #     conn.rollback()
        cursor.close()
        conn.close()
        return item
