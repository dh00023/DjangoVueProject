from django.db import models
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
# 이미지(ImageField)는 settings.MEDIA_ROOT 경로에 파일을 저장하고, DB 필드에는 settings.MEDIA_ROOT내 하위 경로를 저장
class Item(models.Model):
	itemCode = models.CharField("상품코드", max_length=8, primary_key=True)
	itemName = models.CharField("상품명", max_length=100)
	imageUrl = models.URLField("이미지 url") 
	price = models.IntegerField("가격")
	created_at = models.DateTimeField("등록일", auto_now_add=True)

	def __str__(self):
		return self.itemCode

class LookBook(models.Model):
	bnrImageUrl = models.URLField("배너 이미지 url")
	mainImageUrl = models.URLField("LookBook 대표 이미지 url")
	title = models.CharField("제목", max_length=100)
	content = models.TextField("내용")
	items = models.ManyToManyField(Item)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField("등록일", auto_now_add=True)

	def __str__(self):
		return self.title


class Tag(models.Model):
	tag = models.CharField("태그", max_length=20, primary_key=True)
	created_at = models.DateTimeField("등록일", auto_now_add=True)

	def __str__(self):
		return self.tag
	

class StyleShare(models.Model):
	image = models.ImageField("이미지 url")
	items = models.ManyToManyField(Item, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	created_at = models.DateTimeField("등록일", auto_now_add=True)

	def __str__(self):
		return self.author