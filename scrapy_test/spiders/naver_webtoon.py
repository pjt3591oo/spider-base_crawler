# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlparse, parse_qs, urljoin
from ..items import NaverWebtoonsItem
class NaverWebtoonSpider(scrapy.Spider):
    name = 'naver_webtoon'
    start_urls = ['https://comic.naver.com/webtoon/weekday.nhn']

    def start_requests(self):
        print('>>>>>>>>>>>>>>>>>> start request <<<<<<<<<<<<<<<<<<<')
        yield scrapy.http.Request(NaverWebtoonSpider.start_urls[0])

    def parse(self, response):
        webtoons = response.css('.daily_all .col li')

        for webtoon in webtoons:
            a_tag = webtoon.css('.title')
            href = a_tag[0].attrib['href']
            title = a_tag.css('::text').get()

            title_id= parse_qs(urlparse(href).query)['titleId'][0]
            weekday= parse_qs(urlparse(href).query)['weekday'][0]

            naver_weebtoon = NaverWebtoonsItem(
                href = href,
                title_id = title_id,
                weekday = weekday,
                title = title
            )

            yield naver_weebtoon