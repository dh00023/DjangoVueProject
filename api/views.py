from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import requests

from .serializers import LookBookSerializer, StyleShareSerializer, ItemSerializer, TagSerializer
from .models import LookBook, StyleShare, Item, Tag
# CSRF 쿠키중에 ensure_csrf_cookie는 csrf가 기존에 생성되어있으면 그걸 전달, 없으면 새로 생성해준다.
@method_decorator( ensure_csrf_cookie, name='dispatch' )
class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

@method_decorator( ensure_csrf_cookie, name='dispatch' )
class LookBookViewSet(viewsets.ModelViewSet):
	queryset = LookBook.objects.all()
	serializer_class = LookBookSerializer


@method_decorator( ensure_csrf_cookie, name='dispatch' )
class StyleShareViewSet(viewsets.ModelViewSet):
	queryset = StyleShare.objects.all()
	serializer_class = StyleShareSerializer

@method_decorator( ensure_csrf_cookie, name='dispatch' )
class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

def BrandItemList(reqeust):
	url = 'https://search.cjmall.com/search-web/search/cjmall/brandShopItem.json?t=API&isMobile=true&rbc=00004276&o=BEST_SELLING_DESC&s=48&firstSearch=true&isOnload=true&listingType=2&initId=00004276&chn=50001002&srcg=true&srbg=true&srfg=true&srp=true&srcb=true'
	response = requests.get(url)
	return JsonResponse(response.json())