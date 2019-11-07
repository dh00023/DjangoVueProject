from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'lookbook', views.LookBookViewSet)
router.register(r'styleshare', views.StyleShareViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('brandItemList/', views.BrandItemList)
]