from django.contrib import admin
from .models import StyleShare

@admin.register(StyleShare)
class StyleShareAdmin(admin.ModelAdmin):
	list_display = ('user', 'get_items', 'image','created_at')
	list_filter = ['created_at']
	readonly_fields = ['user','created_at']
	
	def get_items(self, request):
		return ",".join([str(item) for item in request.items.all()])

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.user = request.user
			super().save_model(request, obj, form, change)
		else:
			super().save_model(request,obj,form, change)

