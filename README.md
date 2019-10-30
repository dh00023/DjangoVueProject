# New Brand Shop

Python, Django, Vue.js를 이용하여 New Brand Shop을 빠르게 개발.


## 설계

- 브랜드샵 API : http://search.cjmall.com/search-web/search/cjmall/brandShopItem.json?t=API&isMobile=true&rbc=00000252&o=BEST_SELLING_DESC&s=48&firstSearch=true&isOnload=true&listingType=2&initId=00000252&chn=50014001&srcg=true&srbg=true&srfg=true&srp=true&srcb=true

기존의 브랜드샵 API를 이용해 상품 리스트를 가져온다.

- [S.I.Village](http://m.sivillage.com)의 매거진 : 매거진 테이블[사진-(배너용, 하단용), title, content], 상품테이블(상품코드, 이미지, 가격, 상품명)
- [wconcept](http://m.wconcept.co.kr)의 WDNA : 고객들이 직접 입은 스타일 공유( 스타일 선택된 사람들 포인트, 쿠폰 제공 ) - 인스타그램 사진 보여주는 ( 인스타그램 userId를 입력받아 바로 갈 수 있도록 => access token을 가져온 뒤에 사진을 선택해 올릴 수 있도록! ), Style Share 테이블(user id, 인스타그램 id, 사진, 키워드), 키워드 테이블(share table fk, 키워드)


