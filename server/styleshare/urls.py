from django.urls import path
from styleshare import views

app_name = 'styleshare-api'

urlpatterns = [
    path('', views.StyleShareListAPIView.as_view(), name="list"),
    path('create/', views.StyleShareCreateAPIView.as_view(), name="create"),
]