from django.conf import settings
from django.db import models
from django.utils import timezone


# 상품 테이블은 범용적(magazine 테이블, styleshare 테이블)으로 사용하기 위해서 ManyToManyField로 관계를 설정해주는 것이 아니라
# 범용 외래 키 필드(GenericForeignKey)와 범용테이블을 이용할 모델에 범용 관계 필드(GenericRelation)로 관계 설정을 한다.
# https://docs.djangoproject.com/en/2.2/ref/contrib/contenttypes/
#  문제점 : 모델간의 인덱싱이 존재하지 않으면 쿼리속도에 손해,다른 테이블에 존재하지 않는 레코드를 참조할수있는 데이터 충돌 위험성

class Item(models.Model):
	item_code = models.CharField("상품코드", max_length=8, primary_key=True)
	item_name = models.CharField("상품명", max_length=100)
	image_url = models.URLField("이미지 url") 
	price = models.IntegerField("가격")
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField("등록일", auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at"]
		db_table = 'items'

	def __str__(self):
		return 'item Code : "{}", item name : "{}"'.format(self.item_code, self.item_name)