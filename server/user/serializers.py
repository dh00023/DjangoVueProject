from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, authentication
from rest_framework_jwt.settings import api_settings

User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users-api:detail',
        lookup_url_kwarg='user_id'
    )
    
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'email',
            'is_admin',
            'username',
        ]

        
class UserDetailSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'username',
        ]

class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(allow_blank=True, default='')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )
        read_only_fields = ('email',)
        extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance, vaildated_data):
        password = vaildated_data['password'] or None
        if password:
            instance.set_password(password)
        vaildated_data.pop('password', None)

        for field, value in vaildated_data.items():
            if value:
                setattr(instance, field, value)

        instance.save()
        return instance

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
        ]
        extra_kwargs = {"password":{"write_only": True}}
    
    def create(self, vaildated_data):
        email = vaildated_data['email']
        username = vaildated_data['username']
        password = vaildated_data['password']
        user_obj = User(
            email = email,
            username = username
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email = serializers.EmailField(label='Email')
    
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":{"write_only": True}}