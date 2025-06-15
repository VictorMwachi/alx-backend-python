from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    phonenumber = serializers.CharField()
    class Meta:
        model = User
        fields = ['user_id','email','first_name','last_name','phonenumber','full_name']

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
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all(), required=True)
    
    class Meta:
        model = Message
        fields = ['message_id', 'conversation','message_body', 'sender', 'sent_at']

    def validate(self, data):
        if not data.get('conversation_id') and not data.get('recipient_ids'):
            raise serializers.ValidationError("Either 'conversation_id' or 'recipient_ids' must be provided.")
        return data

    def create(self, validated_data):
        validated_data['sender'] = self.context['request'].user
        conversation_id = validated_data.pop('conversation_id', None)
        recipients = validated_data.pop('recipient_ids', [])

        if conversation_id:
            try:
                conversation = Conversation.objects.get(pk=conversation_id)
            except Conversation.DoesNotExist:
                raise serializers.ValidationError({'conversation_id': 'Conversation not found'})
            if not conversation.users.filter(pk=sender.pk).exists():
                raise serializers.ValidationError({'sender': 'You are not a member of this conversation'})
        else:
            participants = list(set(recipients + [sender]))
            existing_conversations = Conversation.objects.annotate(
                user_count=models.Count('users')
            ).filter(user_count=len(participants))

            for conv in existing_conversations:
                if set(conv.users.values_list('pk', flat=True)) == set([u.pk for u in participants]):
                    conversation = conv
                    break
            else:
                conversation = Conversation.objects.create()
                conversation.users.set(participants)

        message = Message.objects.create(conversation=conversation, user=sender, **validated_data)
        return message

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True,read_only = True)
    messages = MessageSerializer(many=True,read_only = True)
    participants_emails = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['conversation_id','participants','messages','participants_emails']

    def get_participants_emails(self, obj):
        return [user.email for user in obj.participants.all()]
    
    def validate(self, data):
        if 'participants' not in data or not data['participants']:
            raise serializers.ValidationError("At least one participant is required.")
        return data