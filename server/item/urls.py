from django.urls import path
from item import views

app_name = 'item-api'

urlpatterns = [
    path('', views.ItemListAPIView.as_view(), name="list"),
    path('create/', views.ItemCreateAPIView.as_view(), name="create"),
    path('<item_code>/edit/', views.ItemUpdateAPIView.as_view(), name="update"),
    path('brand/', views.BrandItemListView),
]