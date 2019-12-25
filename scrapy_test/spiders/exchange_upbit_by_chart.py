# -*- coding: utf-8 -*-
import scrapy, json
from urllib import parse

from ..items import UpbitItem


class ExchangeUpbitByChartSpider(scrapy.Spider):
    name = 'exchange_upbit_by_chart'
    allowed_domains = ['crix-api-cdn.upbit.com']
    start_urls = ['https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/3?code=CRIX.UPBIT.KRW-BTC&count=200&']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    }
    to = "to="

    def __init__(self, **kwargs):
        print('>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<')
        print(**kwargs)

    def start_requests(self):
        print()
        yield scrapy.http.Request(ExchangeUpbitByChartSpider.start_urls[0] + ExchangeUpbitByChartSpider.to, headers=ExchangeUpbitByChartSpider.headers)

    def parse(self, response):
        data_set = json.loads(response.body)

        for data in data_set:

            upbit_item = UpbitItem(
                code = data["code"],
                openingPrice = data["openingPrice"],
                highPrice = data["highPrice"],
                lowPrice = data["lowPrice"],
                tradePrice = data["tradePrice"],
                candleAccTradeVolume = data["candleAccTradeVolume"],
                candleAccTradePrice = data["candleAccTradePrice"],
                unit = data["unit"],
                timestamp = data["timestamp"],
                candleDateTime = data["candleDateTime"],
                candleDateTimeKst = data["candleDateTimeKst"]
            )
            ts = data["candleDateTime"]
            yield upbit_item
        

        # to=2019-12-25T00%3A30%3A00Z
        qs = parse.urlencode([("to", ts.replace('+00:00','Z'))], encoding="UTF-8", doseq=True)
        ExchangeUpbitByChartSpider.to = qs
        url = ExchangeUpbitByChartSpider.start_urls[0] + ExchangeUpbitByChartSpider.to
        
        print(url)
        
        yield scrapy.Request(url, headers=ExchangeUpbitByChartSpider.headers)


# 2019-12-25T00:15:00+00:00
# 2019-12-25T10:18:28Z