from django.urls import path, include

from product import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('product-list/', views.ProductList),
    path('product-list/<str:cat_id>', views.ProductDetail),
    path('category-create/', views.CategoryCreate),
    path('product-create/', views.ProductCreate),
    path('category-list/', views.CategoryList),
]