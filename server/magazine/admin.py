from django.contrib import admin
from .models import Magazine
from item.models import Item

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
	list_display = ('title', 'content',  'get_items', 'created_at', 'user') # 모델의 object
	list_display_links = ['title']
	list_filter = ['created_at'] # 필터기능
	search_fields = ['title'] # 검색기능
	readonly_fields = ["user", "created_at"]
	
	def get_items(self, request):
		return ",".join([str(item) for item in request.items.all()])

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.user = request.user
			super().save_model(request, obj, form, change)
		else:
			super().save_model(request,obj,form, change)
