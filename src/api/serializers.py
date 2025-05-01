from rest_framework import serializers
from rabble.models import *

class SubRabbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRabble
        fields = ['name', 'display_name', 'description', 'community', 'public', 'allow_anonymous']

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    user_display = serializers.StringRelatedField(source='user', read_only=True)
    subrabble_str = serializers.StringRelatedField(source='subrabble.name', read_only=True)
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'user', 'username', 'user_display', 'anonymous', 'subrabble_str']
        read_only_fields = ['user', 'subrabble', 'subrabble_str', 'created_at']

    def create(self, validated_data):
        username = validated_data.pop('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        validated_data['user'] = user
        return super().create(validated_data)