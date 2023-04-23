from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import MenuItemSerilizer, CategorySerializers
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

#from .serializers import MenuItemSerilizer

# Create your views here.

@api_view(['GET','POST'])
def menu_items(request):
    if request.method == 'GET': 
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search:
            items = items.filter(title__contains=search)
        if ordering:
            ordering_fileds = ordering.split(",")
            items = items.order_by(*ordering_fileds)
        serialized_item = MenuItemSerilizer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST': 
        serialized_item = MenuItemSerilizer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def category_item(request):
    if request.method == 'GET': 
        items = Category.objects.all()
        serialized_categories = CategorySerializers(items, many=True)
        return Response(serialized_categories.data)
    if request.method == 'POST': 
        serialized_categories = CategorySerializers(data=request.data)
        serialized_categories.is_valid(raise_exception=True)
        serialized_categories.save()
        return Response(serialized_categories.data, status.HTTP_201_CREATED)
    
    
@api_view()
def single_item(request):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerilizer(item)
    return Response(serialized_item.data)