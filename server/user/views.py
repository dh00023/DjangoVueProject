from django.http import Http404
from rest_framework.status import (
		HTTP_200_OK,
		HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
		CreateAPIView,
		DestroyAPIView,
		ListAPIView,
		UpdateAPIView,
		RetrieveAPIView,
		RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
		AllowAny,
		IsAdminUser,
		IsAuthenticated,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import (
		get_user_model,
		authenticate
)
from .serializers import (
		UserCreateSerializer,
		UserLoginSerializer,
		UserListSerializer,
		UserDetailSeiralizer,
		UserUpdateSerializer
)

User = get_user_model()

class UserListAPIView(ListAPIView):
		queryset = User.objects.all()
		serializer_class = UserListSerializer
		permission_classes = [IsAdminUser]
		
class UserDetailAPIView(RetrieveAPIView):
		queryset = User.objects.all()
		serializer_class = UserDetailSeiralizer
		permission_classes = [IsOwnerOrReadOnly]
		lookup_field = 'id'
		lookup_url_kwarg = 'user_id'

class UserCreateAPIView(CreateAPIView):
		queryset = User.objects.all()
		serializer_class = UserCreateSerializer
		permission_classes = [AllowAny]

class UserUpdateAPIView(UpdateAPIView):
		queryset = User.objects.all()
		serializer_class = UserUpdateSerializer
		permission_classes = [IsOwnerOrReadOnly]
		lookup_field = 'id'
		lookup_url_kwarg = 'user_id'

class UserDeleteAPIView(DestroyAPIView):
		queryset = User.objects.all()
		serializer_class = UserDetailSeiralizer
		permission_classes = [IsOwnerOrReadOnly]
		lookup_field = 'id'
		lookup_url_kwarg = 'user_id'
		
class UserLoginAPIView(APIView):
		serializer_class = UserLoginSerializer
		permission_classes = [AllowAny]
		
		def post(self, request, *args, **kwargs):
				data = request.data
				serializer = UserLoginSerializer(data=data)

				if serializer.is_valid(raise_exception=True):
						user = authenticate(email=serializer.validated_data['email'],
																password=serializer.validated_data['password'])

						if user is not None:
								username = user.username

								jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
								jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

								payload = jwt_payload_handler(user)
								token = jwt_encode_handler(payload)
								# TODO : Fix here!! Important
								return Response({'token': token, 'username': username}, status=HTTP_200_OK)
						else:
								return Response({'msg': 'Credentials are not valid!'}, status=HTTP_400_BAD_REQUEST)
				return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)