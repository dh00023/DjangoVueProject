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
from .models import StyleShare, Tag


class StyleShareListAPIView(ListAPIView):
		serializer_class = StyleShareListSerializer
		permission_classes = [AllowAny]
		#filter_backends = [SearchFilter, OrderingFilter]
		# search_fields = ['user__username']
		queryset = StyleShare.objects.all()


class StyleShareCreateAPIView(CreateAPIView):
		permission_classes = [IsAuthenticated]
		serializer_class = StyleShareCreateUpdateSerializer
		queryset = StyleShare.objects.all()

		def create(self, request, *args, **kwargs):
				serializer = self.get_serializer(data=request.data)
				tags = request.data.getlist('tags')
				for tag in tags:
					t, created = Tag.objects.get_or_create(name=tag)
				
				serializer.is_valid()
				self.perform_create(serializer)
				
				return Response(serializer.data, status=status.HTTP_201_CREATED)

		def perform_create(self, serializer):
			items = self.request.data.getlist('items')
			tags = self.request.data.getlist('tags')
			
			serializer.save(items=items, tags=tags, user=self.request.user)