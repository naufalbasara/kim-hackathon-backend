from django.db import models
import uuid
from django.contrib.auth.models import User
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)


# Create your models here.

class User(
    TimeStampedModel,
    ActivatorModel,
):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    def encode_password(self, password):
        self.password = password
    
