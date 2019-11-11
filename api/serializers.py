from django.contrib.auth.models import User, Group
from .models import Item, LookBook, StyleShare, Tag
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ['itemCode', 'itemName', 'imageUrl', 'price']

class LookBookSerializer(serializers.HyperlinkedModelSerializer):
	items = ItemSerializer(read_only=True, many=True)
	class Meta:
		model = LookBook
		fields = ['id','bnrImageUrl', 'mainImageUrl', 'title', 'content', 'items']

class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		fields = ['tag']
	def create(self, validated_data):
		instance, _ = Tag.objects.get_or_create(**validated_data)
		return instance

class StyleShareSerializer(serializers.HyperlinkedModelSerializer):
	items = ItemSerializer(read_only=True, many=True)
	tags = TagSerializer(read_only=True, many=True)
	imageUrl = serializers.SerializerMethodField('get_image_url')
	
	class Meta:
		model = StyleShare
		fields = ['id', 'imageUrl','items', 'tags']

	def get_image_url(self, obj):
		return obj.image.url

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)