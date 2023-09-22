from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)
# Create your models here.

class User(
    AbstractUser,
    TimeStampedModel,
    ActivatorModel,
):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.email
