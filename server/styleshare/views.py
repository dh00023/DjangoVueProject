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
		StyleShareListSerializer,
		StyleShareCreateUpdateSerializer,
)
from django.db.models import Q
from .models import StyleShare


class StyleShareListAPIView(ListAPIView):
		serializer_class = StyleShareListSerializer
		permission_classes = [AllowAny]
		filter_backends = [SearchFilter, OrderingFilter]
		search_fields = ['user__username']

		def get_queryset(self, *args, **kwargs):
				queryset_list = StyleShare.objects.all()
				query = self.request.GET.get("query")
				if query:
						queryset_list = queryset_list.filter(
								Q(user__username__icontains=query)
						).distinct()
				return queryset_list

class StyleShareCreateAPIView(CreateAPIView):
		permission_classes = [IsAuthenticated]
		serializer_class = StyleShareCreateUpdateSerializer
		queryset = StyleShare.objects.all()

		def perform_create(self, serializer):
			items = self.request.data.getlist('items')
			# tags = self.request.data.getlist('tags')
			# for tag in tags:
			# 	Tag.objects.get_or_create(name=tag)
			# 	import pdb; pdb.set_trace()
			# serializer.save(items=items, tags=tags, user=self.request.user)
			serializer.save(items=items, user=self.request.user)

