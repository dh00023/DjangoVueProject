from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = 	('item_code', 'item_name', 'price',  'image_url', 'get_magazine')
	list_filter = ('item_code', 'item_name')
	search_fields = ('item_code', 'item_name')
	readonly_fields = ["user", "created_at"]

	def get_queryset(self, request):
		qs = super(ItemAdmin, self).get_queryset(request)
		return qs.prefetch_related('magazine_set')

	def get_magazine(self, request):
		return list(request.magazine_set.all())

	# def get_styleshare(self, request):
	# 	return list(request.styleshare_set.all())