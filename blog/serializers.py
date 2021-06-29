from rest_framework import serializers
from .models import Category,Post


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['name']


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['id','title','slug','content','author','category','status']
	# category = CategorySerializer()
