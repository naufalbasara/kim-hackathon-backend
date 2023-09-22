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
    models.Model,
):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'password']

    def __str__(self):
        return self.email


class Order(
    TimeStampedModel,
    ActivatorModel,
    models.Model,
):
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    invoice_number = models.CharField(unique=True, max_length=20)
    design_img = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255)
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=255, default='pending')

    # category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class OrderCustomerDetail(
    TimeStampedModel,
    ActivatorModel,
    models.Model,
):
    class Meta:
        verbose_name = "OrderCustomerDetail"
        verbose_name_plural = "OrderCustomerDetails"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    organization_name = models.CharField(max_length=255)
    organization_website = models.CharField(max_length=255)
