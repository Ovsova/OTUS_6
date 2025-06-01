from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductModelForm, CategoryModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages


def index(request):
    return render(request, 'store_app/index.html')


class ProductListView(ListView):
    model = Product
    template_name = 'store_app/product_list.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    model = Category
    template_name = 'store_app/category_list.html'
    context_object_name = 'category'

class CategoryProductListView(ListView):
    model = Category
    template_name = 'store_app/category_list.html'
    context_object_name = 'category'


class CategoryProductListView(ListView):
    model = Product
    template_name = 'store_app/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store_app/products_detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        product.price = getattr(product, 'price', 0) + 10
        product.save(update_fields=['price'])
        return super().get(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'store_app/add_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успешно добавлен')
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'store_app/edit_product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        messages.success(self.request, 'Продукт успешно обновлен')
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store_app/delete_product.html'
    success_url = reverse_lazy('products')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'store_app/add_category.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('category')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно добавлена')
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'store_app/edit_category.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('category')

    def form_valid(self, form):
        messages.success(self.request, 'Категория успешно обновлен')
        return super().form_valid(form)
