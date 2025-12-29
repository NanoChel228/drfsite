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
        serializer.save()

    
        return Response({"post": serializer.data})
    

    # def delete(self, request):
    #     post = Post.objects.get(id=request.data["id_post"])
    #     return Response({"deleted_post": PostSerializer(post).data})



    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        

        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})
        

        data = PostSerializer(instance).data
        instance.delete()
        return Response({"post": data})
    


# class getPostAPI(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer