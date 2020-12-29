# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["hellobi.com"]
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    # start_urls = ['http://www.douban.com/']
    def start_requests(self):
        return [Request('https://passport.hellobi.com/sso/login', callback=self.parse, meta={"cookiejar":1})]

    def parse(self, response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        url = 'https://passport.hellobi.com/sso/login'
        if len(captcha) > 0:
            print("此时有验证码")
            localpath = "D:/Coding/coding/spider/douban/douban/spiders/result/captcha.png"
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("请查看本地验证码并输入验证码")
            captcha_value = input()
            data = {
                "username": "13802880217",
                "password": "chinamobile",
                "captcha": captcha_value,
                "redir": "https://www.hellobi.com/u/188070"
            }
        else:
            print("此时没有验证码")
            data = {
                "username": "13802880217",
                "password": "chinamobile",
                "redir": "https://www.hellobi.com/u/188070"
            }
        print("登陆中......")
        return [FormRequest.from_response(response, 
                                        meta={"cookiejar":response.meta["cookiejar"]},
                                        headers=self.header,
                                        formdata=data,
                                        callback=self.next)]
    
    def next(self, response):
        print("登陆成功，并爬取个人中心数据")
        title = response.xpath("/html/head/title/text()").extract()
        print(title[0])