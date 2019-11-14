from rest_framework import serializers
from user.serializers import UserDetailSeiralizer
from .models import StyleShare


class StyleShareListSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    class Meta:
        model = StyleShare
        fields = [
            'id',
            'image',
            'items',
            'user',
            'created_at',
        ]
        
class StyleShareDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    class Meta:
        model = StyleShare
        fields = [
            'id',
            'image',
            'items',
            'user',
            'created_at',
        ]


class StyleShareCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleShare
        fields = [
            'image',
            'items',
        ]
