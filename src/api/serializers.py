from rest_framework import serializers
from rabble.models import *

class SubRabbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRabble
        fields = ['name', 'display_name', 'description', 'community', 'public', 'allow_anonymous']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'user', 'anonymous']
        read_only_fields = ['subrabble', 'created_at']