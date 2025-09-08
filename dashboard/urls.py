from django.urls import path, include
from . import views
app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name="dashboard-home"),
    path('user', views.user, name='user'),
    path('user/new', views.add_user, name="add-user"),
    path('user/<int:pk>/edit', views.edit_user, name="edit-user"),
    path('user/<int:pk>/delete', views.delete_user, name="delete-user"),
    path('profile', views.profile, name="profile"),

    path('company/<int:pk>/edit',views.company_edit, name='company-edit'),
    
    path('category', views.category, name="category"),
    path('category/new', views.new_category, name="category-add"),
    path('category/<int:pk>/edit', views.category_edit, name="category-edit"),
    path('category/<int:pk>/delete', views.category_delete, name="category-delete"),

    path('menu', views.menu_item, name="menu-item"),
    path('menu/new', views.add_new_menu_items, name="add-new-menu-items"),
    path('menu/<int:pk>/edit', views.menu_edit, name="menu-edit"),
    path('menu/<int:pk>/delete', views.menu_delete, name="menu-delete"),

    path('orders', views.orders, name="orders"),
    path('salerecord', views.salesrecord, name="sale-record"),

    path('table', views.tables, name="tables"),
    path('table/new', views.table_add, name="table-add"),
    path('table/<int:pk>/edit', views.table_edit, name="table-edit"),
    path('table/<int:pk>/delete', views.table_delete, name="table-delete"),
]
