# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsauto.items import QsautoItem
from scrapy.http import Request


class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://www.qiushibaike.com/']

    rules = (
        Rule(LinkExtractor(allow=r'article/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        yield Request("https://www.qiushibaike.com/", headers=ua)

    def parse_item(self, response):
        i = QsautoItem()
        i["content"] = response.xpath("//div[@class='recmd-right']/a/text()").extract()
        i["link"] = response.xpath("//div[@class='recmd-right']/a/@href").extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        print(i["content"])
        print(i["link"])
        return i
