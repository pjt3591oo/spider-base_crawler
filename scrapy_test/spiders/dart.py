# -*- coding: utf-8 -*-
import scrapy, json
from ..items import DartItem

class DartSpider(scrapy.Spider):
    name = 'dart'
    start_urls = ['http://dart.fss.or.kr/corp/searchCorpL.ax']

    searchIndex = 0 # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16]  # ㄱ~ㅎ, A~Z 검색, 0: ㄱ, 1: ㄴ, ...
    currentPage = 1 # pagination
    last_searchIndex = 16
 
    def start_requests(self):
        yield scrapy.http.FormRequest(
            DartSpider.start_urls[0],
            method='POST', 
            formdata={
                "searchIndex": str(DartSpider.searchIndex),
                "currentPage": str(DartSpider.currentPage)
            }
        )

    def parse(self, response):
        
        table_rows = response.css('.table_scroll table tbody tr')
        
        for row in table_rows:
            office = row.css('input')
            data = row.css('td')
            category = row.css('img')[0].attrib['alt']
            
            office_name = office[0].attrib['value']
            admin_name = data[1].css('::text').get()
            code = data[2].css('::text').get()
            description = data[3].attrib['title']

            dart_item = DartItem(
                category=category,
                office_name=office_name,
                admin_name=admin_name,
                description=description,
                code=code,
            )

            yield dart_item
        
        print('%s %s %s %s %s'%('>'*20,DartSpider.searchIndex, DartSpider.currentPage, len(table_rows), '<'*20,))

        self.next_page()

        if self.is_last_page(table_rows):
            self.reset_page()
            self.next_keyword()

            DartSpider.searchIndex == 14 and self.next_keyword()

        if DartSpider.searchIndex > DartSpider.last_searchIndex:
            return
        
        print('next page request')

        yield scrapy.FormRequest(
            DartSpider.start_urls[0],
            method='POST', 
            formdata={
                "searchIndex": str(DartSpider.searchIndex),
                "currentPage": str(DartSpider.currentPage)
            },
            callback=self.parse
        )

    def next_page(self):
        DartSpider.currentPage += 1
        

    def reset_page(self):
        DartSpider.currentPage = 1

    def is_last_page(self, rows):
        return len(rows) < 300

    def next_keyword(self):
        DartSpider.searchIndex += 1