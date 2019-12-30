# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ShopItem(scrapy.Item):
    storeSeq = scrapy.Field(serializer=str)
    ageNames = scrapy.Field()
    appHit = scrapy.Field()
    cateNames = scrapy.Field()
    description = scrapy.Field()
    webUrl = scrapy.Field()
    storeName = scrapy.Field()
    storeGender = scrapy.Field()
    webProdUrl = scrapy.Field()

class UpbitItem(scrapy.Item):
    code = scrapy.Field()
    openingPrice = scrapy.Field()
    highPrice = scrapy.Field() 
    lowPrice = scrapy.Field() 
    tradePrice = scrapy.Field() 
    candleAccTradeVolume = scrapy.Field() 
    candleAccTradePrice = scrapy.Field() 
    unit = scrapy.Field() 
    timestamp = scrapy.Field() 
    candleDateTime = scrapy.Field() 
    candleDateTimeKst = scrapy.Field()

class CoinoneItem(scrapy.Item):
    dt = scrapy.Field()
    open = scrapy.Field()
    low = scrapy.Field()
    high = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()
    adj_Close = scrapy.Field()

class DartItem(scrapy.Item):
    office_name = scrapy.Field()  # 회사이름
    admin_name = scrapy.Field()   # 대표이름
    description = scrapy.Field()  # 회사설명
    category = scrapy.Field()     # 법인종류
    code = scrapy.Field()         # 종목코드