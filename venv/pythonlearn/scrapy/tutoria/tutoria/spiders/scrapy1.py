#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import sys
import urllib
import urllib.request
import scrapy
from tutoria.items import TutoriaItem
from scrapy.spiders import XMLFeedSpider


# 创建一个类，并继承scrapy的一个子类：scrapy.spider或者是其他蜘蛛类型，
# 除了spider或者其他蜘蛛类型，后面会说到，除了spider还有其他类型
# scrapy crawl example.com -o items.json -t json  结果导出json格式
class scrapy1(XMLFeedSpider):
    name = 'example.com'
    allowed_demains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iterator'
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('hi,this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))
        item = TutoriaItem()
        item['id'] = node.xpath('@id').get()
        item['name'] = node.xpath('name').get()
        item['description'] = node.xpath('description').get()
        return item



