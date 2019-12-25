# -*- coding: utf-8 -*-
import scrapy


class ExchangeUpbitSpider(scrapy.Spider):
    name = 'exchange_upbit'
    allowed_domains = ['https://www.upbit.com/exchange']
    start_urls = ['http://https://www.upbit.com/exchange/']

    def parse(self, response):
        pass
