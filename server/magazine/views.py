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
    MagazineListSerializer,
    MagazineDetailSerializer,
    MagazineCreateUpdateSerializer,
)
from django.db.models import Q
from .models import Magazine


class MagazineListAPIView(ListAPIView):
    serializer_class = MagazineListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__username']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Magazine.objects.all()
        query = self.request.GET.get("query")
        if query:
            queryset_list = queryset_list.filter(
                Q(user__username__icontains=query) |
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return queryset_list

class MagazineDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MagazineDetailSerializer
    queryset = Magazine.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'magazine_id'

class MagazineCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MagazineCreateUpdateSerializer
    queryset = Magazine.objects.all()

    def perform_create(self, serializer):
        # TODO: request get user
        serializer.save(user=self.request.user)

class MagazineUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = MagazineCreateUpdateSerializer
    queryset = Magazine.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'magazine_id'

    def perform_update(self, serializer):
        # TODO: request get user
        serializer.save(user=self.request.user)

class MagazineDeleteAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = MagazineDetailSerializer
    queryset = Magazine.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'magazine_id'