from django.contrib import admin
from .models import Community, CommunityMember, SubRabble, SubRabbleMember, SubRabbleAdmin, Post, Comment, Conversation, ConversationMember, ConversationMessage

admin.site.register(Community)
admin.site.register(CommunityMember)
admin.site.register(SubRabble)
admin.site.register(SubRabbleMember)
admin.site.register(SubRabbleAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Conversation)
admin.site.register(ConversationMember)
admin.site.register(ConversationMessage)
