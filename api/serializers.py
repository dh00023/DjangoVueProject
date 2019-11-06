from django.contrib.auth.models import User, Group
from .models import Item, LookBook, StyleShare
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

class StyleShareSerializer(serializers.HyperlinkedModelSerializer):
	items = ItemSerializer(read_only=True, many=True)
	class Meta:
		model = StyleShare
		fields = ['id','author', 'imageUrl', 'items']