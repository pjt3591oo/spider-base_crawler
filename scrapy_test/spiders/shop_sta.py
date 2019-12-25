# -*- coding: utf-8 -*-
# 스타일닷컴
import scrapy, json, pprint
from ..items import ShopItem

class ShopStaSpider(scrapy.Spider):
    name = 'shop_sta'
    allowed_domains = ['sta1.com']
    start_urls = ['https://api.sta1.com/api/front/v1/stores?ps=60&pg=%d&type=S&gndr=F&ages=&sort=nv']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
        'Accept': 'application/json,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'In-Sess': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YTRmMmQ4Yjc2MDM0OWY2YTRlYjg0NjMwNjJmMzFjNiIsImlhdCI6MTU3NzI3MjQ2MywiZXhwIjoxNTc3Mjc2MDYzLCJob3N0IjoiVyIsImRldmMiOiJQIiwiaXR5cCI6IlIiLCJwc2VxIjoxLCJwY25vIjowLCJvc2VxIjowLCJva3NxIjowLCJpcCI6IjEyMS4xNjEuMTYuMTYxIiwiYXBwaWQiOiIiLCJvc3RwIjoiIiwiYXBwdiI6IiIsInBzaWQiOiIifQ.9dtlvJZpF5n4sblMaaU4cVCK7fSEBSqgzf7dk018I1I'
    }
    current_page = 1

    def start_requests(self):
        yield scrapy.http.Request(ShopStaSpider.start_urls[0]%(ShopStaSpider.current_page), headers=ShopStaSpider.headers)

    def parse(self, response):
        body = json.loads(response.body)
        data_set = body['data']

        for data in data_set:
            shop_item = ShopItem(
                storeSeq=data.get("storeSeq", 0),
                ageNames=data.get("ageNames", ""),
                appHit=data.get("appHit", 0),
                cateNames=str(data.get("cateNames", "")),
                description=str(data.get("description", "")),
                webUrl=str(data.get("webUrl", "")),
                storeName=str(data.get("storeName", "")),
                storeGender=str(data.get("storeGender", "")),
                webProdUrl=str(data.get("webProdUrl", ""))
            )
            yield shop_item

        if not len(data_set):
            return 

        self.nest_page()

        yield scrapy.http.Request(ShopStaSpider.start_urls[0]%(ShopStaSpider.current_page), headers=ShopStaSpider.headers)

    def nest_page(self):
        ShopStaSpider.current_page += 1


