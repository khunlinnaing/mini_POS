from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import LoginAPIView, RegisterView

schema_view = get_schema_view(
   openapi.Info(
      title="Mini POS",
      default_version='v1',
      description="API documentation using Swagger",
      terms_of_service="https://www.linkedin.com/in/khun-lin-naing-oo-4272a4255/",
      contact=openapi.Contact(email="khunlinnaing90@email.com"),
      license=openapi.License(name="KLNO License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # URL path for the login API
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]