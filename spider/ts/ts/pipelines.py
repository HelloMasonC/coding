# -*- coding: utf-8 -*-
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):
    def __init__(self):
        self.fl = open("D:/Coding/coding/spider/ts/ts/spiders/lesson_result.txt", "a")

    def process_item(self, item, spider):
        title = "标题: {}".format(item["title"][0])
        print(title)
        link = "链接: {}".format(item["link"][0])
        print(link)
        stu_nums = "学习人数: {}".format(re.findall(r"\d+\.?\d*", item["stu_nums"][0])[0])
        print(stu_nums)
        print("------")
        self.fl.write(title + "\n" + link + "\n" + stu_nums + "\n" + "------" + "\n")
        return item

    def close_spider(self):
        self.fl.close()
