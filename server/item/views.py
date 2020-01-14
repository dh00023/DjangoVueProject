from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .serializers import (
    ItemListSerializer,
    ItemCreateUpdateSerializer,
)
from django.db.models import Q
from .models import Item
from django.http import JsonResponse
import requests

class ItemListAPIView(ListAPIView):
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['item_code', 'item_name', 'user__username']
    queryset = Item.objects.all()


class ItemCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemCreateUpdateSerializer
    queryset = Item.objects.all()

    def perform_create(self, serializer):
        # TODO: request get user
        serializer.save(user=self.request.user)

class ItemUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ItemCreateUpdateSerializer
    queryset = Item.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'item_code'

    def perform_update(self, serializer):
        # TODO: request get user
        serializer.save(user=self.request.user)

def BrandItemListView(reqeust):
	url = 'https://search.cjmall.com/search-web/search/cjmall/brandShopItem.json?t=API&isMobile=true&rbc=00004276&o=BEST_SELLING_DESC&s=48&firstSearch=true&isOnload=true&listingType=2&initId=00004276&chn=50001002&srcg=true&srbg=true&srfg=true&srp=true&srcb=true'
	response = requests.get(url)
	return JsonResponse(response.json())