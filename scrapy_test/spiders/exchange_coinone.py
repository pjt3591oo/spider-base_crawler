# -*- coding: utf-8 -*-
import scrapy, json
from ..items import CoinoneItem


class ExchangeCoinoneSpider(scrapy.Spider):
    name = 'exchange_coinone'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    }
    allowed_domains = ['coinone.co.kr']
    start_urls = ['https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinone%s&type=%s&last_time=%s'] # btc, 1m

    def start_requests(self):
        url = ExchangeCoinoneSpider.start_urls[0]%('eth', '1m', '')
        print(url)
        yield scrapy.http.Request(url, headers=ExchangeCoinoneSpider.headers)

    def parse(self, response):
        data_set = json.loads(response.body)
        data_set['data'].reverse()
        
        for data in data_set['data'][:-1]:
            coinone_item = CoinoneItem(
                dt = data['DT'],
                open = data['Open'],
                low = data['Low'],
                high = data['High'],
                close = data['Close'],
                volume = data['Volume'],
                adj_Close = data['Adj_Close']
            )
            
            yield coinone_item
        
        print('\n')
        url = ExchangeCoinoneSpider.start_urls[0]%('eth', '1m', data_set['data'][-1]['DT'])
        print(url)

        yield scrapy.Request(url, headers=ExchangeCoinoneSpider.headers)