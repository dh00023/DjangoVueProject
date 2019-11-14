from rest_framework import serializers
from user.serializers import UserDetailSeiralizer
from .models import Magazine


class MagazineListSerializer(serializers.ModelSerializer):
    user = UserDetailSeiralizer(read_only=True)
    class Meta:
        model = Magazine
        fields = [
            'id',
            'bnr_image_url',
            'main_image_url',
            'title',
            'content',
            'user',
            'created_at',
        ]