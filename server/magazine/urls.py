from django.urls import path
from magazine import views

app_name = 'magzines-api'

urlpatterns = [
    path('', views.MagazineListAPIView.as_view(), name="list")
]