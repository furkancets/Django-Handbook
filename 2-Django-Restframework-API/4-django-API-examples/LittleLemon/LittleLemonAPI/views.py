from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilizer
    
class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilizer
