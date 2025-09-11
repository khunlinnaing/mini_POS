from django.urls import path, include
from . import views

app_name="website"

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # for social login
    path('', views.index, name="index"),
    path('logout', views.logout_view, name="logout-view"),
    path('login', views.login_view, name="login-view"),
    path('register', views.register_view, name='register-view'),

    path('menuites/', views.menu_item, name="menu-item"),
    path('create/', views.create_order, name='create-order'),
    path('status/<int:order_id>/', views.order_status, name='order_status'),
]