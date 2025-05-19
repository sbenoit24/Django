import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    chat_count = models.PositiveIntegerField(default=0)

class ChatSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or str(self.id)

class ChatMessage(models.Model):
    SENDER_CHOICES = (
        ('USER', 'User'),
        ('AI', 'AI'),
    )

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
