from json import JSONDecodeError
import random
from django.http import JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from .serializer import OrderSerializer,  OrderCustomerDetailSerializer
from .models import Order, OrderCustomerDetail
from django.db import IntegrityError


@api_view(['GET'])
def HomeView(request):
    return Response({
        "Status": status.HTTP_200_OK,
        "Message": "KIM-Hackathon API Scheme"
    })


class AuthenticationView(views.APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user is None:
            return Response({
                "Message": "Failed to login",
                "Status": status.HTTP_401_UNAUTHORIZED
            })

        return Response({
            "Message": "Successfully Authenticated",
            "Status": status.HTTP_200_OK
        })


def generate_unique_invoice_number():
    while True:
        invoice_number = "INV-" + str(random.randint(100000, 999999))
        try:
            invoice_number = Order.objects.get(invoice_number=invoice_number)
            if invoice_number:
                continue
            else:
                return invoice_number
        except IntegrityError:
            continue


class OrderView(
    views.APIView,
):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        try:
            data = request.data

            # Create random Invoice Number

            invoice_number = generate_unique_invoice_number()

            order = {
                "invoice_number": invoice_number,
                "design_img": data['design_img'],
                # "category_id": data['category_id'],
                "size": data['size'],
                "quantity": data['quantity'],
                "description": data['description'],
            }

            order_serializer = OrderSerializer(data=order)

            if order_serializer.is_valid():
                order_serializer.save()
            else:
                return Response(
                    {
                        "error": order_serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            order_customer_detail = {
                "order": {
                    "type": "Order",
                    "id": order_serializer.data['id']
                },
                "customer_name": data['customer_name'],
                "customer_email": data['customer_email'],
                "customer_phone": data['customer_phone'],
                "organization_name": data['organization_name'],
                "organization_website": data['organization_website'],
            }

            order_customer_detail_serializer = OrderCustomerDetailSerializer(
                data=order_customer_detail)

            if order_customer_detail_serializer.is_valid():

                order_customer_detail_serializer.save()
                return JsonResponse(
                    order_serializer.data, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "error": order_customer_detail_serializer.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return JsonResponse(
                {"error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
