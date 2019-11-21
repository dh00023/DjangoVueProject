from rest_framework import serializers
from user.serializers import UserDetailSeiralizer
from item.serializers import ItemCreateUpdateSerializer, ItemDetailSerializer
from .models import StyleShare



class StyleShareListSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    items = ItemDetailSerializer(read_only=True, many=True)
    class Meta:
        model = StyleShare
        fields = [
            'id',
            'image',
            'items',
            'user',
            'created_at',
        ]
        
# class TagCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = [
#             'name'
#         ]

class StyleShareCreateUpdateSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    class Meta:
        model = StyleShare
        fields = [
            'image',
            'items',
            'user',
            'created_at',
        ]
