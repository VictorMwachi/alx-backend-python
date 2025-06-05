from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','email','first_name','last_name','phonenumber']

class ConversationSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True,querysets=User.objects.all())
    class Meta:
        model = Conversation
        fields = ['conversation_id','users']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['message_id','conversation_id','user_id','message_body','sent_at']