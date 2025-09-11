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

def item_swagger(operation_description="", tagname="", requestdata=None, method="GET"):
    if method.upper() in ["POST", "PUT", "DELETE"]:
        return swagger_auto_schema(
            operation_description=operation_description,
            tags=[tagname],
            manual_parameters=[token_param],
            request_body=requestdata
        )
    else:
        return swagger_auto_schema(
            operation_description=operation_description,
            tags=[tagname],
            manual_parameters=[token_param]
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

    @item_swagger("Get all companies", "Company", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single company", "Company", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new company", "Company", requestdata=CompanySerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("Update company", "Company", requestdata=CompanySerializer, method="PUT")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("Delete company", "Company", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all userprofiles", "UserProfile", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single userprofile", "UserProfile", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new userprofile", "UserProfile", requestdata=UserProfileSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update userprofile", "UserProfile", requestdata=UserProfileSerializer, method='PUT')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete userprofile", "UserProfile", method='DELETE')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @item_swagger("Get all categories", "Category", method='GET')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single category", "Category", method='GET')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new category", "Category", requestdata=CategorySerializer, method='POST')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update category", "Category", requestdata=CategorySerializer, method="PUT")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete category", "Category", method='DELETE')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all items", "Item", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single item", "Item", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new item", "Item", requestdata=ItemSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update item", "Item", requestdata=ItemSerializer, method="POST")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete item", "Item", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all tables", "Table", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single table", "Table", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new table", "Table", requestdata=TableSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update table", "Table", requestdata=TableSerializer, method="PUT")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete table", "Table", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all orders", "Order", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single order", "Order", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new order", "Order", requestdata=OrderSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update order", "Order", requestdata=OrderSerializer, method="PUT")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete order", "Order", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all orderitems", "OrderItem", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single orderitem", "OrderItem", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new orderitem", "OrderItem", requestdata=OrderItemSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update orderitem", "OrderItem", requestdata=OrderItemSerializer, method="PUT")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete orderitem", "OrderItem", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all customers", "Customer", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single customer", "Customer", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new customer", "Customer", requestdata=CustomerSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update customer", "Customer", requestdata=CustomerSerializer, method="PUT")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete customer", "Customer", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

    @item_swagger("Get all sales", "Sales", method="GET")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @item_swagger("Get a single sales", "Sales", method="GET")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @item_swagger("Create new sales", "Sales", requestdata=SaleSerializer, method="POST")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @item_swagger("update sales", "Sales", requestdata=SaleSerializer, method="POST")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @item_swagger("delete sales", "Sales", method="DELETE")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

