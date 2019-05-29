#!/usr/bin/python
# -*- encoding: utf-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # 可以回到tutoria 根目录运行 scrapy crawl quotes 查看包含【tutoria】的输出

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]   #【-2】不是参数，会对返回的列表进行索引，选取倒数第二项
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
