# Run

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