from rest_framework import serializers
from .models import Chat, ChatAdmin, Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'chat_name', 'chat_memebers_count', 'chat_owner')

class ChatAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatAdmin
        fields = ('id', 'chat', 'admin_chat')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message_text', 'message_time', 'sender', 'chat')