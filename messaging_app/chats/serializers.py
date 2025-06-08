from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phonenumber = serializers.CharField()
    class Meta:
        model = User
        fields = ['user_id','email','full_name','phonenumber']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    def validate_email(self, value):
        if not value.endswith('.com'):
            serializers.ValidationError('Valid email required')
        return value
    
    def validate_phonenumber(self, value):
        if not value.isdigit():
            serializers.ValidationError('Valid phonenumber required')
        return value
        
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['message_id','conversation_id','user_id','sender','message_body','sent_at']

class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True,read_only = True)
    messages = MessageSerializer(many=True,read_only = True)
    class Meta:
        model = Conversation
        fields = ['conversation_id','users','messages']