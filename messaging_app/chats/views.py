from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Conversation, Message
from .serializers import ConversationSerializer,  MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    #permission_classes = [IsAuthenticated]
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['participants']

    def get_queryset(self):
        # Only show conversations the user belongs to
        return Conversation.objects.filter(participants=self.request.user)

    def perform_create(self, serializer):
        serializer.save()  
    
    def create(self, request, *args, **kwargs):
        participants_emails = request.data.get('participants', [])
        if not participants_emails:
            return Response(
                {"detail": "At least one participant is required."},
                 status=status.HTTP_400_BAD_REQUEST
                 )
        # Ensure participants are valid users
        participants = User.objects.filter(email__in=participants_emails)
        if participants.count() != len(participants_emails):
            return Response(
                {"detail": "One or more participants do not exist."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if request.user not in participants:
            participants = list(participants) + [request.user.email]

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        # Only show messages in conversations the user belongs to
        return Message.objects.filter(conversation__users=self.request.user)

    def perform_create(self, serializer):
        serializer.save()  
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)