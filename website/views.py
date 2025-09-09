from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate, login
from django.contrib import messages
from dashboard.formsFiles.userForms import UserForm
from dashboard.models import Category, Item


def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    moreitem = int(request.GET.get('more', 8))


    if category_id:
        try:
            selected_category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            selected_category = categories.first()
    else:
        selected_category = categories.first()

    if selected_category:
        menu_items = Item.objects.filter(category=selected_category, is_available=True).order_by('-id')[:moreitem]

    else:
        menu_items = []

    context = {
        'categories': categories,
        'menu_items': menu_items,
        'selected_category': selected_category,
        'item_length': Item.objects.filter(category=selected_category, is_available=True).count(),
        'current': moreitem,
    }

    return render(request, 'index.html', context)


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
