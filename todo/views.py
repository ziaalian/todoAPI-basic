import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response (serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['POST'])
def postUpdate(request,pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def postDelete(request, pk):
    posts = Post.objects.get(id=pk)
    posts.delete()
    return Response("Item is Deleted")