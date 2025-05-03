from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category


def index(request):
    return render(request, 'store_app/index.html')

def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store_app.product_list.html', context=context)


def category_list(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'store_app.category_list.html', context=context)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'store_app.category_products.html', context=context)

def products_detail(request, product_id ):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'store_app.products_detail.html', context=context)
