from rest_framework_json_api import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

from .models import User, Order,  OrderCustomerDetail, TestImage




class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderCustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCustomerDetail
        fields = '__all__'


class TestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestImage
        fields = '__all__'
