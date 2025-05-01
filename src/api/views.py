from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rabble.models import *
from .serializers import *

@api_view(['GET'])
def subrabble_list(request):
    if request.method == 'GET':
        subrabbles = SubRabble.objects.all()
        serializer = SubRabbleSerializer(subrabbles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def subrabble_detail(request, identifier):
    try:
        subrabble = SubRabble.objects.get(name=identifier)
    except SubRabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubRabbleSerializer(subrabble)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def subrabble_post_list(request, identifier):
    try:
        subrabble = SubRabble.objects.get(name=identifier)
    except SubRabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        posts = Post.objects.filter(subrabble=subrabble)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(subrabble=subrabble)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def subrabble_post_detail(request, identifier, post_pk):
    try:
        subrabble = SubRabble.objects.get(name=identifier)
        post = Post.objects.get(pk=post_pk, subrabble=subrabble)
    except (SubRabble.DoesNotExist, Post.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)