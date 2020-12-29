# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem


class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://www.dangdang.com/']

    def parse(self, response):
        pass
