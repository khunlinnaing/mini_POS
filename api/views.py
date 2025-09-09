from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from .serializersFolder.authserializers import *
from .serializers import *

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_description="User login",
        tags=["Auth"],
        request_body=LoginSerializer,
    )
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            user_data = UserSerializer(user).data
        
            return Response({
                    'message': 'User registered successfully.',
                    'token': token.key,
                    'user': user_data
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "Invalid credentials. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

class RegisterView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_description="User registration",
        tags=["Auth"],
        request_body=RegisterSerializer,
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
