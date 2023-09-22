from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


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