from rest_framework import serializers
from user.serializers import UserDetailSeiralizer
from item.serializers import ItemDetailSerializer
from .models import Magazine


class MagazineListSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    items = ItemDetailSerializer(read_only=True, many=True)
    class Meta:
        model = Magazine
        fields = [
            'id',
            'bnr_image_url',
            'main_image_url',
            'title',
            'content',
            'user',
            'items',
            'created_at',
        ]