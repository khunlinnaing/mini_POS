from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        print("hello Post")
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
        
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )
    def get(self, request):
        print("Hello Get")

class RegisterView(APIView):
    """
    API endpoint for user registration.
    Allows unauthenticated users to register a new account via a POST request.
    """
    # The AllowAny permission class ensures that anyone can access this view,
    # as they need to be unauthenticated to create a new account.
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles the POST request for user registration.
        Validates the request data using the UserSerializer and saves the new user.
        Returns a success response if the user is created, otherwise returns validation errors.
        """
        # Initialize the serializer with the request data.
        serializer = UserSerializer(data=request.data)

        # Use the is_valid() method to check if the data meets the serializer's requirements.
        # This will run the built-in and custom validation rules.
        if serializer.is_valid():
            # If valid, save the user. This will call the serializer's create() method.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If the data is not valid, return the errors with a 400 Bad Request status code.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
