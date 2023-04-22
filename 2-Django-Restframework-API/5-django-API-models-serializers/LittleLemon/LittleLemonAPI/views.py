from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerilizer
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics

#from .serializers import MenuItemSerilizer

# Create your views here.

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerilizer(items, many=True)
    return Response(serialized_item.data)
