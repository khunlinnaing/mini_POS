from django.urls import path, include
from .views import LoginAPIView, RegisterView

urlpatterns = [
    # URL path for the login API
    path('/login/', LoginAPIView.as_view(), name='login'),
    path('/register/', RegisterView.as_view(), name='register'),
]