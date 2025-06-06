from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

# Create your models here.
class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    username = None
    email = models.EmailField(unique=True,null=False)
    first_name = models.CharField(max_length=25,null=False)
    last_name = models.CharField(max_length=25,null=False)
    password = models.CharField(max_length=128,validators=[MinLengthValidator(8)])
    phone_number = models.CharField(max_length=15,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email
    
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    users = models.ManyToManyField(User,related_name='conversations')
    
    def __str__(self):
        return str(self.conversation_id)
    
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='messages')
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,related_name='messages')
    message_body = models.CharField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} sent at: {self.sent_at} by: {self.user}"