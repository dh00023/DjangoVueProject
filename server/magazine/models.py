from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone

# Manager는 데이터베이스와 상호작용하는 인터페이스
# Magazine.objects.all() 다음과 같이 접근하는데 이때 objects를 customize
class MagazineManager(models.Manager):
		# connection을 이용해서 sql문을 직접 작성할 수 있다.
		# def with_counts(self):
	 #      from django.db import connection
	 #      with connection.cursor() as cursor:
	 #          cursor.execute("""
	 #              SELECT p.id, p.question, p.poll_date, COUNT(*)
	 #              FROM polls_opinionpoll p, polls_response r
	 #              WHERE p.id = r.poll_id
	 #              GROUP BY p.id, p.question, p.poll_date
	 #              ORDER BY p.poll_date DESC""")
	 #          result_list = []
	 #          for row in cursor.fetchall():
	 #              p = self.model(id=row[0], question=row[1], poll_date=row[2])
	 #              p.num_responses = row[3]
	 #              result_list.append(p)
	 #      return result_list
		def active(self, *args, **kwargs):
				return super(MagazineManager, self).filter(created_at__lte=timezone.now())

# TODO: image upload field
class Magazine(models.Model):
	bnr_image_url = models.URLField("배너 이미지 url")
	main_image_url = models.URLField("LookBook 대표 이미지 url")
	title = models.CharField("제목", max_length=100)
	content = models.TextField("내용")
	# items = models.ManyToManyField(Item)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField("등록일", auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = MagazineManager()

	class Meta:
		ordering = ["-created_at"]
		db_table = 'magazines'

	def __str__(self):
		return 'magzine title : "{}"'.format(self.title)

	@property
	def get_content_type(self):
		instance = self
		content_type = ContentType.objects.get_for_model(instance.__class__)
		return content_type

		# @property
	#   def comments(self):
	#       instance = self
	#       qs = Comment.objects.filter_by_instance(instance)
	#       return qs