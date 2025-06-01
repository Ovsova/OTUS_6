from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='products_detail'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/<int:category_id>/', views.CategoryProductListView.as_view(), name='category_products'),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit_product'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('add_category/', views.CategoryCreateView.as_view(), name='add_category'),
    path('category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='edit_category'),
]
