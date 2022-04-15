from datetime import datetime
from django.db import models

class Chat(models.Model):
    chat_name = models.CharField(max_length=100)
    chat_memebers_count = models.IntegerField(default=2)
    chat_owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def _str_(self):
        return self.chat_name

class ChatAdmin(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    admin_chat = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Message(models.Model):
    message_text = models.CharField(max_length=280)
    message_time = models.DateTimeField(default=datetime.now)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    member = models.ForeignKey('auth.User', on_delete=models.CASCADE)