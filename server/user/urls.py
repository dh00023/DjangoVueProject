from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user import views

app_name = 'users-api'

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='list'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('register/', views.UserCreateAPIView.as_view(), name="register"),
    path('<int:user_id>/', views.UserDetailAPIView.as_view(), name='detail'),
    path('<int:user_id>/edit/', views.UserUpdateAPIView.as_view(), name='edit'),
    path('<int:user_id>/delete/', views.UserDeleteAPIView.as_view(), name='delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)