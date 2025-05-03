from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products_list, name='products'),
    path('products/<int:product_id>/', views.products_detail, name='products_detail'),
    path('category/', views.category_list, name='category'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),

]
