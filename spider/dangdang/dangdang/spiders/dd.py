# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request


class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    custom_settings = {
        'DOWNLOAD_DELAY': 4,
        'CONCURRENT_REQUESTS': 1
    }
    # start_urls = ['http://www.dangdang.com/']

    def start_requests(self):
        yield Request("http://category.dangdang.com/cp01.47.03.00.00.00.html", headers=self.ua)

    def parse(self, response):
        item = DangdangItem()
        item['title'] = response.xpath("//ul[@class='bigimg']/li/p[@class='name']/a/text()").extract()
        item['link'] = response.xpath("//ul[@class='bigimg']/li/p[@class='name']/a/@href").extract()
        item['cost'] = response.xpath("//ul[@class='bigimg']/li/p[@class='price']/span[@class='search_now_price']/text()").extract()
        item['bookshop'] = response.xpath("//ul[@class='bigimg']/li/p[@class='search_shangjia']/a/@title").extract()
        item['comment'] = response.xpath("//ul[@class='bigimg']/li/p[@class='search_star_line']/a/text()").extract()
        yield item
        for i in range(2, 11):
            url = "http://category.dangdang.com/pg" + str(i) + "-cp01.47.03.00.00.00.html"
            yield Request(url, callback=self.parse, headers=self.ua)
