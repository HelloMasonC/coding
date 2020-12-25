# -*- coding: utf-8 -*-
import scrapy
from spider01.items import Spider01Item
from scrapy.http import Request


class QsbkSpider(scrapy.Spider):
    name = "qsbk"
    allowed_domains = ["qiushibaike.com"]
    # start_urls = ['http://www.qiushibaike.com/']

    def start_requests(self):
        ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        yield Request("https://www.qiushibaike.com/", headers=ua)

    def parse(self, response):
        item = Spider01Item()
        item["content"] = response.xpath("//div[@class='recmd-right']/a/text()").extract()
        item["link"] = response.xpath("//div[@class='recmd-right']/a/@href").extract()
        yield item
