from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .serializers import (
    StyleshareListSerializer,
    StyleshareCreateUpdateSerializer,
)
from django.db.models import Q
from .models import Styleshare


class StyleshareListAPIView(ListAPIView):
    serializer_class = StyleshareListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__username']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Styleshare.objects.all()
        query = self.request.GET.get("query")
        if query:
            queryset_list = queryset_list.filter(
                Q(user__username__icontains=query) |
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return queryset_list

class StyleshareDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = StyleshareDetailSerializer
    queryset = Styleshare.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'styleshare_id'

class StyleshareCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StyleshareCreateUpdateSerializer
    queryset = Styleshare.objects.all()

    def perform_create(self, serializer):
        # TODO: request get user
        serializer.save(user=self.request.user)