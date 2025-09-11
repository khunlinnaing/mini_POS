from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import logout,authenticate, login
from django.contrib import messages
from dashboard.formsFiles.userForms import UserForm
from django.forms import modelformset_factory
from .forms import *
from dashboard.models import *

def safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
    
def index(request):
    categories = Category.objects.all()
    print(request.POST)
    category_id = safe_int(request.POST.get('category_id', 0))
    moreitem = safe_int(request.POST.get('more'),8)

    if category_id !=0:
        try:
            selected_category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            selected_category = None
    else:
        selected_category = None

    if selected_category:
        menu_items = Item.objects.filter(category=selected_category, is_available=True).order_by('-id')[:moreitem]
    else:
        menu_items = Item.objects.filter(is_available=True).order_by('-id')[:moreitem]

    context = {
        'categories': categories,
        'menu_items': menu_items,
        'selected_category': selected_category,
        'item_length': selected_category.items.filter(is_available=True).count() if  selected_category else Item.objects.filter(is_available=True).count(),
        'current': moreitem,
    }

    return render(request, 'index.html', context)

def menu_item(request):
    return render(request, './pages/bookingpage.html')

def logout_view(request):
    logout(request)
    return redirect('website:index')

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('website:index')  # Change to your home URL
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'authpages/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('website:login-view')
    else:
        form = UserForm()
    return render(request, 'authpages/register.html', {'form': form})



def create_order(request):
    items = Item.objects.all()

    if request.method == "POST":
        order = Order.objects.create(
            waiter=request.user,
            total_amount=0,  # We will calculate this
        )

        total = 0
        for item in items:
            qty = int(request.POST.get(f'item_{item.id}', 0))
            if qty > 0:
                subtotal = qty * item.price
                OrderItem.objects.create(
                    order=order,
                    item=item,
                    quantity=qty,
                    price_at_order=item.price,
                    subtotal=subtotal
                )
                total += subtotal

        order.total_amount = total
        order.save()

        messages.success(request, "Order Created Successfully!")
        return redirect('website:order_status', order_id=order.pk)  # Change this to your actual URL name

    return render(request, 'orders/create_order.html', {'items': items})


# ✅ Order status ကြည့်ရန် view
def order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    return render(request, 'orders/order_status.html', {
        'order': order
    })