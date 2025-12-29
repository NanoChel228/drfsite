from django.utils import timezone
import io
from rest_framework import serializers
from .models import Post
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class PostModel:
#     def __init__(self, title, text):
#         self.title = title
#         self.text = text


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    text = serializers.CharField()
    created_ta = serializers.DateTimeField(default=timezone.now, read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.text = validated_data.get("text", instance.text)
        instance.created_ta = validated_data.get("created_ta", instance.created_ta)
        instance.save()
        return instance
    

    


# def encode():
#     model = PostModel('Dollar is Stronger and stronger', 'text: The US dollar is now stronger than ever before...')
#     model_sr = PostSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


# def decode():
#     stream = io.BytesIO(b'{"title":"Dollar is Stronger and stronger","text":"text: The US dollar is now stronger than ever before..."}')
#     data = JSONParser().parse(stream)
#     serializer = PostSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)