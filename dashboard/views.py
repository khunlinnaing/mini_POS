from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse

from .formsFiles.categoryForms import *
from .formsFiles.menuitemForms import *
from .formsFiles.tableForms import *

from .formsFiles.companyForms import *
from .formsFiles.userForms import *
from .models import *


@login_required
def dashboard_home(request):
    return render(request, 'compoments/mainpage.html')

''' start of user section '''
@login_required
def user(request):
    user_list = User.objects.all().select_related('profile')
    paginator = Paginator(user_list, 10)  # Show 10 users per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/index.html', {
        'user_objects': page_obj
    })

@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:user')
    else:
        form = UserForm()
    
    return render(request, 'users/post.html', {'form': form})

@login_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard:user')
    else:
        form = EditUserForm(instance=user)
    return render(request, 'users/patch.html', {'form': form})

@login_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user:
        user.delete()
        return redirect('dashboard:user')
    
@login_required
def profile(request):
    return render(request, 'users/profile.html')

''' end of user section section '''

''' start of compangy section '''
@login_required
def company_edit(request,pk):
    company = get_object_or_404(Company, pk=pk)

    if request.method == 'POST':
        form = EditCompanyForm(request.POST, request.FILES,instance=company)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard:dashboard-home'))
    else:
        form = EditCompanyForm(instance=company)
    return render(request, 'company/index.html', {'form': form})

''' end of compangy section '''

''' start company setion'''
@login_required
def category(request):
    category_list = Category.objects.all()
    paginator = Paginator(category_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'category/index.html', {
        'category_objects': page_obj
    })

@login_required
def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:category')
    else:
        form = CategoryForm()
    return render(request, 'category/newcategory.html', {'form': form})

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = EditCategoryForm(request.POST, request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard:category')
    else:
        form = EditCategoryForm(instance=category)
    return render(request, 'category/editcategory.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if category:
        category.delete()
        return redirect(f"{reverse('category')}?page={request.GET.get('page', 1)}")

''' end of company section '''

"""Start of MenuItem section """
@login_required
def menu_item(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menus/index.html', {
        'items_objects': page_obj
    })

@login_required
def add_new_menu_items(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:menu-item')
    else:
        form = MenuItemForm()
    return render(request, 'menus/newmenu.html', {'form': form})

@login_required
def menu_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = EditMenuItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard:menu-item')
    else:
        form = EditMenuItemForm(instance=item)
    return render(request, 'menus/editmenu.html', {'form': form})

@login_required
def menu_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item:
        item.delete()
        return redirect(f"{reverse('dashboard:menu-item')}?page={request.GET.get('page', 1)}")
    
"""Start of MenuItem section """

 
@login_required
def orders(request):
    return render(request, 'orders/index.html')

@login_required
def salesrecord(request):
    return render(request, 'salesrecord/index.html')

"""Start of Table section """
@login_required
def tables(request):
    table_list = Table.objects.all()
    paginator = Paginator(table_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tables/index.html', {
        'tables_objects': page_obj
    })

@login_required
def table_add(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:tables')
    else:
        form = TableForm()
    return render(request, 'tables/newtable.html', {'form': form})

@login_required
def table_edit(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == 'POST':
        form = EditTableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('dashboard:tables')
    else:
        form = EditTableForm(instance=table)
    return render(request, 'tables/edittable.html', {'form': form})

@login_required
def table_delete(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if table:
        table.delete()
        return redirect(f"{reverse('tables')}?page={request.GET.get('page', 1)}")
"""End of Table section """