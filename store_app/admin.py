from django.contrib import admin
from .models import Product, Category
# Register your models here.

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'category')
    ordering = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'category',)
