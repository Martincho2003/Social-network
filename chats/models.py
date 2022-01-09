from django.db import models

class Chat(models.Model):
    chat_name = models.CharField(max_length=100)

class Message(models.Model):
    message_text = models.CharField()
    message_time = models.DateTimeField()
    sender_id = models.ForeignKey(auth_user)
    chat_id = models.ForeignKey(Chat)