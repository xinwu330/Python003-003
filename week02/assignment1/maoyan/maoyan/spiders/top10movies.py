# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class Top10moviesSpider(scrapy.Spider):
    name = 'top10movies'
    allowed_domains = []
    start_urls = ['file:///Users/Admin/Desktop/maoyanhtml.html']
    # allowed_domains = ['maoyan.com']
    # start_urls = ['https://maoyan.com/films']
    # base_url = 'https://maoyan.com'

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        print(response)
        selector = Selector(response=response)
        links = selector.xpath('//div[@class="channel-detail movie-item-title"]/a/@href').getall()[:10]
        print(links)
        # for link in links:
        #     url = self.base_url + link
        #     yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        item = MaoyanItem()
        selector = Selector(response=response)
        movie_brief = selector.xpath('//div[@class="movie-brief-container"]')
        movie_name = movie_brief.xpath('./h1/text()').get()
        movie_types_list = movie_brief.xpath('.//a/text()').getall()
        movie_types = ''
        for moive_type in movie_types_list:
            movie_types += moive_type.strip() + ' '
        movie_release_date = movie_brief.xpath('.//li[last()]/text()').get()
        item['movie_name'] = movie_name
        item['movie_types'] = movie_types
        item['movie_release_date'] = movie_release_date
        print(item)
        yield item