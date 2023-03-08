from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from django.shortcuts import get_object_or_404


@api_view(['Get','POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True, context={'request': request})
        return Response(serialized_item.data)
    
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data, context={'request': request})
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view()
def single_item(request, pk):
    item = get_object_or_404(MenuItem, id=pk)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)
