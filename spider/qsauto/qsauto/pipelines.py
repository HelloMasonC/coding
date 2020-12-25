# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QsautoPipeline(object):
    def process_item(self, item, spider):
        # for i in range(0, len(item["content"])):
        #     print("{0}标题：{1};".format(i+1, item["content"][i]))
        #     print("{0}链接：https://www.qiushibaike.com{1}。".format(i+1, item["link"][i]))
        return item
