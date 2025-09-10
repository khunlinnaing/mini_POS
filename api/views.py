from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .serializersFolder.authserializers import *
from .serializers import *
from drf_yasg import openapi

def item_swagger(operation_description="", tagname="", requestdata=''):
    return swagger_auto_schema(
        operation_description=operation_description,
        tags=[tagname],
        manual_parameters=[token_param],
        request_body=requestdata
    )

token_param = openapi.Parameter(
    name='Authorization',
    in_=openapi.IN_HEADER,
    description='Token <your_token>',
    type=openapi.TYPE_STRING,
    required=True
)

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

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all companies", "Company")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single company", "Company")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new company", "Company")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update company", "Company")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete company", "Company")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all userprofiles", "UserProfile")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single userprofile", "UserProfile")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new userprofile", "UserProfile")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update userprofile", "UserProfile")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete userprofile", "UserProfile")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @item_swagger("Get all categories", "Category")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single category", "Category")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new category", "Category")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update category", "Category")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete category", "Category")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all items", "Item")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single item", "Item")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new item", "Item")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update item", "Item")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete item", "Item")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all tables", "Table")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single table", "Table")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new table", "Table")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update table", "Table")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete table", "Table")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all orders", "Order")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single order", "Order")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new order", "Order")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update order", "Order")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete order", "Order")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all orderitems", "OrderItem")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single orderitem", "OrderItem")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new orderitem", "OrderItem")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update orderitem", "OrderItem")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete orderitem", "OrderItem")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all customers", "Customer")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single customer", "Customer")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new customer", "Customer")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update customer", "Customer")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete customer", "Customer")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all sales", "Sales")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single sales", "Sales")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new sales", "Sales")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update sales", "Sales")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete sales", "Sales")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

