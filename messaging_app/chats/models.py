from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinLengthValidator

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True,null=False)
    username = None  # Disable username field
    first_name = models.CharField(max_length=25,null=False)
    last_name = models.CharField(max_length=25,null=False)
    password = models.CharField(max_length=128,validators=[MinLengthValidator(8)])
    phone_number = models.CharField(max_length=15,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    participants = models.ManyToManyField(User,related_name='conversations')

    def __str__(self):
        return str(self.conversation_id)
    
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='messages')
    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,related_name='messages')
    message_body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} sent at: {self.sent_at} by: {self.user}"