from django.contrib import admin
from .models import User, ChatSession, ChatMessage
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(ChatSession)
admin.site.register(ChatMessage)
