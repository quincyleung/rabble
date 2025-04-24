from django.contrib import admin
from .models import User, UserFollower, Community, CommunityMember, SubRabble, SubRabbleMember, SubRabbleAdmin, Post, Comment, Like, Conversation, ConversationMember, ConversationMessage

admin.site.register(User)
admin.site.register(UserFollower)
admin.site.register(Community)
admin.site.register(CommunityMember)
admin.site.register(SubRabble)
admin.site.register(SubRabbleMember)
admin.site.register(SubRabbleAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Conversation)
admin.site.register(ConversationMember)
admin.site.register(ConversationMessage)
