# New Brand Shop

Python, Django, Vue.js를 이용하여 New Brand Shop을 빠르게 개발.

- vue 서버 실행

```console
$ npm run serve
```

- django 서버 실행

```console
$ ./manage.py runserver
```

각각 서버를 실행한 후에 [http://localhost:8000](http://localhost:8000)으로 접속하면된다.

- data 추가하기

```console
$ ./manage.py loaddata api/fixtures/data.json
```

- db migrations and data 삭제하기

```console
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete
$ rm -rf config/db.sqlite3
```

## 설계

- 브랜드샵 API : http://search.cjmall.com/search-web/search/cjmall/brandShopItem.json?t=API&isMobile=true&rbc=00000252&o=BEST_SELLING_DESC&s=48&firstSearch=true&isOnload=true&listingType=2&initId=00000252&chn=50014001&srcg=true&srbg=true&srfg=true&srp=true&srcb=true

기존의 브랜드샵 API를 이용해 상품 리스트를 가져온다.

- [S.I.Village](http://m.sivillage.com)의 매거진 : 매거진 테이블[사진-(배너용, 하단용), title, content], 상품테이블(상품코드, 이미지, 가격, 상품명)
- [wconcept](http://m.wconcept.co.kr)의 WDNA : 고객들이 직접 입은 스타일 공유( 스타일 선택된 사람들 포인트, 쿠폰 제공 ) - 인스타그램 사진 보여주는 ( 인스타그램 userId를 입력받아 바로 갈 수 있도록 => access token을 가져온 뒤에 사진을 선택해 올릴 수 있도록! ), Style Share 테이블(user id, 인스타그램 id, 사진, 키워드), 키워드 테이블(share table fk, 키워드)

- 무신사스토어 스냅(길거리, 스탭) => 담당 MD나 쇼호스트 스냅으로 해서 올릴 수 있는( 관련 상품 올리고 comment 달 수 있는 )


### 테이블

User 1 : N LookBook
User 1 : N StyleShare

LookBook N : M Item

styleshare N : M Item
styleshare 1 : N keyword

여기서는 프로토타입으로 간편하게 만들기 위해서 1:N관계로 모델 설계를 했지만 추후에 N:M 관계로 확장할 수 있다.

#### User

| field | comment |
|----------|----------|
|username | id |
|email | 이메일|
|password | 비밀번호 |


#### LookBook

| field | comment |
|----------|----------|
|id|index|
|title|타이틀|
|content|내용|
|bnrImageUrl|매거진페이지 배너 이미지|
|mainImageUrl|매거진페이지 메인 이미지|
|items| many to many |
|user_id|foreign key|


#### item

| field | comment |
|----------|----------|
|itemCode| 상품코드(pk)|
|image| 상품 이미지|
|price|가격|
|itemName|상품명|

#### styleShare

| field | comment |
|----------|----------|
|id|index|
|author| instagramUserName|
|imageUrl| 게시글 등록 이미지 |
|items|many to many|
|user_id|foreign key|


#### keyword

| field | comment |
|----------|----------|
|id|index|
|keyword|키워드 내용|
|styleshare_id|foreign key|

### API

- 브랜드샵 상품 리스트 불러오는 ( 기존 cjmall api )
- 장고로 구현
	- lookbook(list, detail)
	- styleShare(list, detail)


| url | view | method | |
|----------|----------|----------|----------|
| /api/lookbook/ | | | magazine api(rest_framework)|
| /api/styleshare/ | | | styleshare api(rest_framework)|

### Page

front쪽은 Vue만을 이용해서 구현한다.

| url | view | method | |
|----------|----------|----------|----------|
| /||| index page |
| /lookbook/|||magazine list 페이지(index)|
| /styleshare/|||style share list 페이지(index)|

