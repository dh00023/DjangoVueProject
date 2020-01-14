from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from .serializers import MagazineListSerializer

# from django.db.models import Q
from .models import Magazine


class MagazineListAPIView(ListAPIView):
    serializer_class = MagazineListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__username']
    queryset = Magazine.objects.all()

    # query params를 받아오는! 그걸로 다음과 같이 필터링을 걸 수 있다.
    # icontains는 ILIKE >> 대소문자 무시 비교
    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Magazine.objects.all()
    #     query = self.request.query_params.get('id')
    #     import pdb; pdb.set_trace()
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(user__username__icontains=query) |
    #             Q(title__icontains=query) |
    #             Q(content__icontains=query)
    #         ).distinct()
    #     return queryset_list
