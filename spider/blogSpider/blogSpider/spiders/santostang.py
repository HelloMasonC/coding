# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from blogSpider.items import BlogspiderItem

class SantostangSpider(scrapy.Spider):
    name = "santostang"
    allowed_domains = ["www.santostang.com"]
    start_urls = ['http://www.santostang.com/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        # first_title = soup.find("h1", class_="post-title").a.text.strip()
        # title_list = soup.findAll("h1", class_="post-title")
        # print("第一篇文章的标题是：", first_title)
        # for i in range(len(title_list)):
        #     title = title_list[i].a.text.strip()
        #     print('第%s篇文章的标题是：%s' %(i+1, title))

        # items = []
        # title_list = soup.find_all("h1", class_="post-title")
        # for i in range(len(title_list)):
        #     item = BlogspiderItem()
        #     title = title_list[i].a.text.strip()
        #     link = title_list[i].a["href"]
        #     item["title"] = title
        #     item["link"] = link
        #     items.append(item)
        # return items

        title_list = soup.find_all("h1", class_="post-title")
        for i in range(len(title_list)):
            item = BlogspiderItem()
            title = title_list[i].a.text.strip()
            link = title_list[i].a["href"]
            # 变成字典
            item["title"] = title
            item["link"] = link
            # 根据文章链接，发送Request请求，并传递item参数
            yield scrapy.Request(url=link, meta={'item':item}, callback=self.parse2)
        
    def parse2(self, response):
        # 接收传递的item
        item = response.meta['item']
        soup = BeautifulSoup(response.text, "lxml")
        content = soup.find("div", class_="view-content").text.strip()
        content = content.replace("\n", "")
        item["content"] = content
        yield item