from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    company_name = models.CharField(default='A')
    company_logo = models.ImageField(upload_to='companylogo/')
    company_address = models.CharField()

    def __str__(self):
        return self.company_name

class UserProfile(models.Model):
    STAFF_LEVEL_CHOICES = [
        (0, 'Staff'),
        (1, 'Manager'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company', default=1)
    phone = models.CharField()
    profile = models.ImageField(upload_to='profile/')
    staff_level = models.IntegerField(choices=STAFF_LEVEL_CHOICES, default=0)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    """
    POS System မှာ ရောင်းချမယ့် အစားအသောက်ပစ္စည်းများ
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # ဈေးနှုန်း (ဥပမာ: 1500.50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    is_available = models.BooleanField(default=False) # ပစ္စည်းရှိ/မရှိ (ရောင်းရန် အသင့်)
    image = models.ImageField(upload_to='item_images/') # ပစ္စည်းရဲ့ ပုံ

    def __str__(self):
        return self.name

class Table(models.Model):

    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField(default=4) # ထိုင်ခုံအရေအတွက်
    is_occupied = models.BooleanField(default=False) # စားပွဲ ပြီးပြီလား

    def __str__(self):
        return f"Table {self.table_number}"

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    order_time = models.DateTimeField(auto_now_add=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, related_name='orders') # ဘယ်စားပွဲက မှာတာလဲ
    waiter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders_taken') # မှာယူပေးတဲ့ ဝန်ထမ်း
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} - Table {self.table.table_number if self.table else 'N/A'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_at_order = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price_at_order
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} for Order #{self.order.pk}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Sale(models.Model):
    sale_time = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='sale')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, blank=True, null=True) 
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')

    def __str__(self):
        return f"Sale #{self.pk} for Order #{self.order.pk}"
