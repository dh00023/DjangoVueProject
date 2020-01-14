from django.conf import settings
from django.db import models
from django.utils import timezone

from item.models import Item


class Tag(models.Model):
	name = models.CharField("태그", max_length=15, primary_key=True)

# Create your models here.
class StyleShare(models.Model):
	image = models.ImageField("이미지 url", null=True, blank=True)
	items = models.ManyToManyField(Item, null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	created_at = models.DateTimeField("등록일", auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.image.path

	class Meta:
		ordering = ["created_at"]
		db_table = 'styleshare'