from rest_framework import status
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
        'Update Product': '/product-update/<str:pk>/',
        'Delete Category': '/category-delete/<str:pk>/',
        'Delete Product': '/product-delete/<str:pk>/',
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


@api_view(['POST'])
def ProductUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductCreateSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def CategoryDelete(request, pk):
    try:
        category = Category.objects.get(id=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def ProductDelete(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


