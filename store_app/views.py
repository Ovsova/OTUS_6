from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductModelForm, CategoryModelForm

def index(request):
    return render(request, 'store_app/index.html')

def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store_app/product_list.html', context=context)


def category_list(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'store_app/category_list.html', context=context)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store_app/category_products.html', context=context)

def products_detail(request, product_id ):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'store_app/products_detail.html', context=context)

def add_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductModelForm()

    context = {'form': form, 'title': 'Добавить продукт'}
    return render(request, 'store_app/add_product.html', context=context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductModelForm(instance=product)

    context = {'form': form, 'title': 'Отредактировать продукт'}
    return render(request, 'store_app/edit_product.html', context=context)



def add_category(request):
    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryModelForm()

    context = {'form': form, 'title': 'Добавить категорию'}
    return render(request, 'store_app/add_category.html', context=context)

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryModelForm(instance=category)

    context = {'form': form, 'title': 'Отредактировать категорию'}
    return render(request, 'store_app/edit_category.html', context=context)