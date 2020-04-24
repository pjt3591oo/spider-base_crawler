# Run

* regular

```
$ scrapy crawl [크롤러 이름]
```

크롤러 이름은 **`spiders`**에 있는 파일명을 적는다. 전달 옵션에 따라 다양한 형태로 저장가능하며 pipelines를 통해서도 저장할 수 있다.

## 스타일닷컴

* 구동

```bash
$ scrapy crawl shop_sta
```

* json 저장

```bash
$ scrapy crawl shop_sta -o result.json
```

* csv 저장

```bash
$ scrapy crawl shop_sta -o result.csv -t csv
```

스타일 닷컴에서 쇼핑몰 리스트 수집


```json
{
  "storeSeq": "24", 
  "ageNames": "30대", 
  "appHit": 896, 
  "cateNames": "미시스타일,심플베이직", 
  "description": "세련되고 엘레강스한 여성의류 쇼핑몰. 깔끔한 핏의 하이퀄리티 아이템 판매", 
  "webUrl": "http://www.annanblue.com/", 
  "storeName": "안나앤블루", 
  "storeGender": "F", 
  "webProdUrl": "/shop/shopdetail.html"
}
```

## 업비트

* 구동

```bash
$ scrapy crawl exchange_upbit_by_chart
```

* json 저장

```bash
$ scrapy crawl exchange_upbit_by_chart -o result.json
```

* csv 저장

```bash
$ scrapy crawl exchange_upbit_by_chart -o result.csv -t csv
```

## 코인원

* 구동

```bash
$ scrapy crawl exchange_coinone
```

* json 저장

```bash
$ scrapy crawl exchange_coinone -o result.json
```

* csv 저장

```bash
$ scrapy crawl exchange_coinone -o result.csv -t csv
```

## 전자공시 시스템

* 구동

```bash
$ scrapy crawl dart
```

* json 저장

```bash
$ scrapy crawl dart -o dart.json
```

* csv 저장

```bash
$ scrapy crawl dart -o dart.csv -t csv
```

## 네이버 웹툰 리스트

* 구동

```bash
$ scrapy crawl naver_webtoon
```

* json 저장

```bash
$ scrapy crawl naver_webtoon -o webtoon.csv
```

* csv 저장

```bash
$ scrapy crawl naver_webtoon -o webtoon.csv -t csv    
```


# crawler generator

```bash
$ scrapy genspider [크롤러 이름] [링크]
```

**`spiders`** 아래에 [크롤러 이름] 파일이 생성되며 다음과 같이 내용을 채움

```py
import scrapy


class ExchangeUpbitSpider(scrapy.Spider):
    name = 'exchange_upbit'
    allowed_domains = ['https://www.upbit.com/exchange']
    start_urls = ['http://https://www.upbit.com/exchange/']

    def parse(self, response):
        pass

```

전달된 링크가 **`allowed_domains`**, **`start_urls`** 값으로 전달된다.
