from rest_framework import generics
from django.shortcuts import render

from .serializers import PostSerializer
from .models import Post

# Create your views here.
class getPostAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer