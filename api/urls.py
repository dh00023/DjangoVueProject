from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'lookbook', views.LookBookViewSet)
router.register(r'styleshare', views.StyleShareViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'tag', views.TagViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('brandItemList/', views.BrandItemList)
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)