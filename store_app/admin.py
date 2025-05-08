from django.contrib import admin
from .models import Product, Category
from django import forms
# Register your models here.

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'category')
    ordering = ('name',)
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name',)

    @admin.action(description='Поменять цену на +100 ')
    def cange_price_upper(self, request, queryset):
        for product in queryset:
            product.price += 100
            product.save()
        self.message_user(request, 'Цена изменилась')
    @admin.action(description='Поменять цену на -100 ')
    def cange_price_downer(self, request, queryset):
        for product in queryset:
            product.price -= 100
            product.save()
        self.message_user(request, 'Цена изменилась')
    actions = ('cange_price_upper', 'cange_price_downer')


