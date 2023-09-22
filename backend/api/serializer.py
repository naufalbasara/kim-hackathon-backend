from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

from .models import User, Category, Order,  OrderCustomerDetail

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
class OrderCustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCustomerDetail
        fields = '__all__'