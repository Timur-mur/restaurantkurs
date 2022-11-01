from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, ProductCreateSerializer, CategoryCreateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Product List': '/product-list/',
        'Product Detail': '/product-list/<str:cat_id>',
        'Category List': '/category-list/',
        'Create Category': '/category-create/',
        'Create Product': '/product-create/',
        'Update': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def ProductList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductDetail(request, cat_id):
    products = Product.objects.all().filter(category=cat_id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CategoryList(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CategoryCreate(request):
    serializer = CategoryCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def ProductCreate(request):
    serializer = ProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)