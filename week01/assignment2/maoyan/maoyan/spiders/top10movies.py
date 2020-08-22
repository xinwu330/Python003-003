# -*- coding: utf-8 -*-
import scrapy


class Top10moviesSpider(scrapy.Spider):
    name = 'top10movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
