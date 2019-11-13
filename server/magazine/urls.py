from django.urls import path
from magazine import views

app_name = 'magzines-api'

urlpatterns = [
    path('', views.MagazineListAPIView.as_view(), name="list"),
    path('create/', views.MagazineCreateAPIView.as_view(), name="create"),
    path('<int:magazine_id>/', views.MagazineDetailAPIView.as_view(), name="detail"),
    path('<int:magazine_id>/edit/', views.MagazineUpdateAPIView.as_view(), name="update"),
    path('<int:magazine_id>/delete/', views.MagazineDeleteAPIView.as_view(), name="delete"),
]