from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets

from .serializers import LookBookSerializer, StyleShareSerializer
from .models import LookBook, StyleShare
# CSRF 쿠키중에 ensure_csrf_cookie는 csrf가 기존에 생성되어있으면 그걸 전달, 없으면 새로 생성해준다.
@method_decorator( ensure_csrf_cookie, name='dispatch' )
class LookBookViewSet(viewsets.ModelViewSet):
	queryset = LookBook.objects.all()
	serializer_class = LookBookSerializer


@method_decorator( ensure_csrf_cookie, name='dispatch' )
class StyleShareViewSet(viewsets.ModelViewSet):
	queryset = StyleShare.objects.all()
	serializer_class = StyleShareSerializer