# New Brand Shop

Python, Django, Vue.js를 이용하여 New Brand Shop을 빠르게 개발.


## 설계

- 브랜드샵 API : http://search.cjmall.com/search-web/search/cjmall/brandShopItem.json?t=API&isMobile=true&rbc=00000252&o=BEST_SELLING_DESC&s=48&firstSearch=true&isOnload=true&listingType=2&initId=00000252&chn=50014001&srcg=true&srbg=true&srfg=true&srp=true&srcb=true

기존의 브랜드샵 API를 이용해 상품 리스트를 가져온다.

- [S.I.Village](http://m.sivillage.com)의 매거진 : 매거진 테이블[사진-(배너용, 하단용), title, content], 상품테이블(상품코드, 이미지, 가격, 상품명)
- [wconcept](http://m.wconcept.co.kr)의 WDNA : 고객들이 직접 입은 스타일 공유( 스타일 선택된 사람들 포인트, 쿠폰 제공 ) - 인스타그램 사진 보여주는 ( 인스타그램 userId를 입력받아 바로 갈 수 있도록 => access token을 가져온 뒤에 사진을 선택해 올릴 수 있도록! ), Style Share 테이블(user id, 인스타그램 id, 사진, 키워드), 키워드 테이블(share table fk, 키워드)

- 무신사스토어 스냅(길거리, 스탭) => 담당 MD나 쇼호스트 스냅으로 해서 올릴 수 있는( 관련 상품 올리고 comment 달 수 있는 )


### 테이블

USER 1 : N Magazine
USER 1 : N styleshare

Magazine N : N Item

styleshare N : N Item
styleshare 1 : N keyword

여기서는 프로토타입으로 간편하게 만들기 위해서 1:N관계로 모델 설계를 했지만 추후에 N:M 관계로 확장할 수 있다.

#### User

| field | comment |
|----------|----------|
|username | id |
|email | 이메일|
|password | 비밀번호 |


#### Magazine

| field | comment |
|----------|----------|
|id|index|
|title|타이틀|
|content|내용|
|bnrPhoto|매거진페이지 배너 이미지|
|mainPhoto|매거진페이지 메인 이미지|
|user_id|foreign key|

#### MagazineDetail

| field | comment |
|----------|----------|
|id|index|
|html|wsywyg로 작성한 기술서|
|magazine_id|foreign key|

#### item

| field | comment |
|----------|----------|
|itemCode(id)| 상품코드|
|image| 상품 이미지|
|price|가격|
|itemName|상품명|
|magazie_id | ForeignKey|
|styleShare_id | ForeignKey|

#### styleShare

| field | comment |
|----------|----------|
|id|index|
|username| instagramUserName|
|itemCode|상품테이블 foriegn key|
|mediaUrl| 게시글 등록 이미지 |
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
	- magazine(list, detail)
	- styleShare(list, detail)


| url | view | method | |
|----------|----------|----------|----------|
| /api/megazine/ | | | magazine api(rest_framework)|
| /api/styleshare/ | | | styleshare api(rest_framework)|

| url | view | method | |
|----------|----------|----------|----------|
| / | | | index 페이지 |
| /magazine/|||magazine list 페이지(index)|
| /magazine/{id}|||magazine detail page|
| /styleShare/|||style share list 페이지(index)|
| /styleShare/id|||style share detail page|


## Image Field

- pillow

Python Image Library 일종으로 파이썬으로 이미지를 처리하고 싶을 때 사용한다. 이미지 관련 width, height, format, resize 작업을 수행

```console
$ pip install pillow
```