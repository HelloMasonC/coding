# -*- coding: utf-8 -*-
import scrapy
from spider01.items import Spider01Item


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        item = Spider01Item()
        item["content"] = response.xpath("/html/head/title/text()").extract()
        yield item
