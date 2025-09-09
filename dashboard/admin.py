from django.contrib import admin
from .models import *
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Company model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('id','company_name', 'company_address', 'company_logo')
    search_fields = ('company_name', 'company_address')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','profile','staff_level', 'company')
    search_fields = ('user',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Item model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_available')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Table model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('table_number', 'capacity', 'is_occupied')
    list_filter = ('is_occupied',)
    search_fields = ('table_number',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Order model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('id', 'table', 'waiter', 'total_amount', 'status', 'payment_status', 'order_time')
    list_filter = ('status', 'payment_status', 'order_time')
    search_fields = ('table__table_number', 'waiter__username')
    raw_id_fields = ('table', 'waiter') # Related objects တွေများလာရင် အမြန်ရှာဖွေနိုင်ဖို့
    readonly_fields = ('total_amount',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    OrderItem model ကို admin panel မှာ စီမံခွဲရန်။
    """
    list_display = ('order', 'item', 'quantity', 'price_at_order', 'subtotal')
    list_filter = ('order', 'item')
    search_fields = ('order__id', 'item__name')
    readonly_fields = ('subtotal',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customer model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'phone_number', 'email')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """
    Sale model ကို admin panel မှာ စီမံခန့်ခွဲရန်။
    """
    list_display = ('sale_time', 'order', 'amount_paid', 'payment_method', 'customer')
    list_filter = ('payment_method',)
    search_fields = ('order__id', 'customer__name')
    raw_id_fields = ('order', 'customer')
