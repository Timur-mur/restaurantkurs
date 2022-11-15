from django.urls import path, include

from product import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('product-list/', views.ProductList),
    path('product-list/<str:cat_id>', views.ProductDetail),
    path('category-create/', views.CategoryCreate, name="cat_create"),
    path('product-create/', views.ProductCreate, name="prod_create"),
    path('category-list/', views.CategoryList),
    path('product-update/<str:pk>', views.ProductUpdate),
    path('category-delete/<str:pk>', views.CategoryDelete),
    path('product-delete/<str:pk>', views.ProductDelete),
    path('orders', views.OrdersView),
    path('orders-delete/<str:pk>', views.DeleteOrder),
]