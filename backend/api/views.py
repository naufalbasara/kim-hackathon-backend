from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import views, status, generics
from rest_framework.response import Response


class AuthenticationView(generics.GenericAPIView):
    pass
