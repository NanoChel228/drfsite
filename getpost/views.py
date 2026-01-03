from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .serializers import PostSerializer
from .models import Post

# Create your views here.


class PostViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Post.objects.all()[:3]

        return Post.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def titlePost(self, request, pk=None):
        posts = Post.objects.get(pk=pk)
        return Response({"post_title": posts.title})
        # return Response({"posts": [p.title for p in posts]})







# class getPostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class getPostAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class getPostAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class getPostAPI(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         return Response({"posts": PostSerializer(posts, many=True).data})
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

    
#         return Response({"post": serializer.data})
    

#     # def delete(self, request):
#     #     post = Post.objects.get(id=request.data["id_post"])
#     #     return Response({"deleted_post": PostSerializer(post).data})



#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
        

#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
    

#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
        

#         data = PostSerializer(instance).data
#         instance.delete()
#         return Response({"post": data})
    


# class getPostAPI(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer