from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email
    
class message(models.Model):
    pass
class conversation(models.Model):
    pass