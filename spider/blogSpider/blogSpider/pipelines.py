# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BlogspiderPipeline(object):
    file_path = "D:\\Coding\\coding\\spider\\blogSpider\\result.txt"

    def __init__(self):
        self.article = open(self.file_path, "a+", encoding="utf-8")

    def process_item(self, item, spider):
        # title = item["title"]
        # link = item["link"]
        # output = title + '\t' + link + '\n'
        # self.article.write(output)
        # return item
        title = item["title"]
        link = item["link"]
        content = item["content"]
        output = title + '\t' + link + '\t' + content + '\n\n'
        self.article.write(output)
        return item
