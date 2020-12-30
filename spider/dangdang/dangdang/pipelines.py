# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            cost = item['cost'][i]
            bookshop = item['bookshop'][i]
            comment = item['comment'][i]
            print(title + "\n" + link + "\n" + cost + "\n" + bookshop + "\n" + comment + "\n")
        return item
