from django.contrib import admin
from django import forms
from . import models

# Register your models here.
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
	fields = ('itemCode', 'itemName', 'price', 'imageUrl')
	list_display = 	('itemCode', 'itemName', 'price', 'lookbook', 'styleshare', 'imageUrl')
	list_filter = ('itemCode', 'itemName')
	search_fields = ('itemCode', 'itemName')

	def get_queryset(self, request):
		qs = super(ItemAdmin, self).get_queryset(request)
		return qs.prefetch_related('lookbook_set', 'styleshare_set')

	def lookbook(self, request):
		return list(request.lookbook_set.all())

	def styleshare(self, request):
		return list(request.styleshare_set.all())


@admin.register(models.LookBook)
class LookBookAdmin(admin.ModelAdmin):
	# fields = ['title', 'bnrImageUrl', 'mainImageUrl', 'content'] # 모델 필드 순서
	list_display = ('title', 'content',  'get_items', 'created_at') # 모델의 object
	list_display_links = ['title']
	list_filter = ['created_at'] # 필터기능
	search_fields = ['title'] # 검색기능
	exclude = ['user',]
	
	def get_items(self, request):
		return ",".join([str(item) for item in request.items.all()])

	
	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.user = request.user
			super().save_model(request, obj, form, change)
	# inline이 있는 경우에만 inline form 노출
	# def get_formsets_with_inlines(self, request, obj=None):
	# 	for inline in self.get_inline_instances(request, obj):
	# 		if not isinstance(inline, ItemInline) or obj is not None:
	# 			yield inline.get_formset(request, obj), inline

@admin.register(models.StyleShare)
class StyleShareAdmin(admin.ModelAdmin):
	list_display = ('author', 'get_items', 'imageUrl','created_at') # 모델의 object
	list_filter = ['created_at'] # 필터기능
	search_fields = ['author'] # 검색기능
	exclude = ['user',]
	
	def get_items(self, request):
		return ",".join([str(item) for item in request.items.all()])

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.user = request.user
			super().save_model(request, obj, form, change)
# # admin.site.register(models.LookBook, LookBookAdmin)
