from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    avatar_url = models.TextField(blank=True, null=True)

class UserFollower(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete= models.CASCADE, related_name='folowers')

    class Meta:
        unique_together = ('user', 'follower')

class Community(models.Model):
    name = models.TextField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_communities')
    admins = models.ManyToManyField(User, related_name='admin_communities')

class CommunityMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'community_id')

class SubRabble(models.Model):
    name = models.TextField(unique=True)
    display_name = models.TextField()
    description = models.TextField()
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    allow_anonymous = models.BooleanField(default=False)

class SubRabbleMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble = models.ForeignKey(SubRabble, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'subrabble')

class SubRabbleAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble = models.ForeignKey(SubRabble, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'subrabble')

class Post(models.Model):
    title = models.TextField()
    body = models.TextField()
    subrabble = models.ForeignKey(SubRabble, on_delete=models.CASCADE, related_name="posts")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

class Conversation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey('Community', on_delete=models.CASCADE)

class ConversationMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'conversation')

class ConversationMessage(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)