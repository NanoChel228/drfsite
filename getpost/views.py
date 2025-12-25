from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post

# Create your views here.

class getPostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({"posts": PostSerializer(posts, many=True).data})
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        post_new = Post.objects.create(
            title=request.data["title"],
            text=request.data["text"],
        )
        return Response({"post": PostSerializer(post_new).data})



# class getPostAPI(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer