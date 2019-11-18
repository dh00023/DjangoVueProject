from rest_framework import serializers
from user.serializers import UserDetailSeiralizer
from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    class Meta:
        model = Item
        fields = [
            'item_code',
            'image_url',
            'price',
            'user',
            'created_at',
        ]

class ItemDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    class Meta:
        model = Item
        fields = [
            'item_code',
            'image_url',
            'price',
            'user',
            'created_at',
        ]

class ItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'item_code',
            'image_url',
            'price',
        ]