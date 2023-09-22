from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response


class HelloView(views.APIView):
    def get(self, request):
        return Response({
            'message': 'API is working'
        })
