from django.urls import path
from item import views

app_name = 'item-api'

urlpatterns = [
    path('', views.ItemListAPIView.as_view(), name="list"),
    path('create/', views.ItemCreateAPIView.as_view(), name="create"),
]