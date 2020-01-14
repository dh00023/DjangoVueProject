from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = 	('item_code', 'item_name', 'price',  'image_url', 'get_magazine', 'get_styleshare')
	list_filter = ('item_code', 'item_name')
	search_fields = ('item_code', 'item_name')
	readonly_fields = ['user', 'created_at']

	def get_queryset(self, request):
		qs = super(ItemAdmin, self).get_queryset(request)
		return qs.prefetch_related('magazine_set', 'styleshare_set')

	def get_magazine(self, request):
		return list(request.magazine_set.all())

	def get_styleshare(self, request):
		return list(request.styleshare_set.all())

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)



# admin.site.register(Item)