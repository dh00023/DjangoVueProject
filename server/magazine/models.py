from django.conf import settings
from django.db import models
from django.utils import timezone

from item.models import Item

# Manager는 데이터베이스와 상호작용하는 인터페이스
# Magazine.objects.all() 다음과 같이 접근하는데 이때 objects를 customize 할 수 있다.
class MagazineManager(models.Manager):
		def active(self, *args, **kwargs):
				return super(MagazineManager, self).filter(created_at__lte=timezone.now())

class Magazine(models.Model):
	bnr_image_url = models.URLField("배너 이미지 url")
	main_image_url = models.URLField("LookBook 대표 이미지 url")
	title = models.CharField("제목", max_length=100)
	content = models.TextField("내용")
	items = models.ManyToManyField(Item)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField("등록일", auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = MagazineManager()

	class Meta:
		ordering = ["-created_at"]
		db_table = 'magazines'

	def __str__(self):
		return 'magzine title : "{}"'.format(self.title)