from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer,CategorySerializer
from .models import Post,Category
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import (BasePermission,IsAdminUser,IsAuthenticated,SAFE_METHODS)


class PostUserWritePermission(BasePermission):
	message = 'Editing posts is restricted to author only'

	def has_object_permission(self, request, view, obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.author == request.user

"""Implementing Viewsets"""

#ModelViewSet
class PostList(viewsets.ModelViewSet):
	permission_classes = [PostUserWritePermission]
	serializer_class = PostSerializer

	def get_object(self,queryset=None,**kwargs):
		item = self.kwargs.get('pk')
		return get_object_or_404(Post,slug=item)
	#Define custom queryset
	def get_queryset(self):
		return Post.objects.all()




"""
#ViewSet
class PostList(viewsets.ViewSet):
	permission_classes = [IsAuthenticated]
	queryset = Post.postobjects.all()

	def list(self,request):
		serializer_class = PostSerializer(self.queryset, many=True)
		return Response(serializer_class.data)

	def retrieve(self,request,pk=None):
		post = get_object_or_404(self.queryset,pk=pk)
		serializer_class = PostSerializer(post)
		return Response(serializer_class.data)
"""
"""
#generic API view

class PostList(generics.ListCreateAPIView):

	permission_classes = [IsAuthenticated]
	queryset = Post.postobjects.all()
	serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView,PostUserWritePermission):

	permission_classes = [PostUserWritePermission]
	queryset = Post.postobjects.all()
	serializer_class = PostSerializer
"""