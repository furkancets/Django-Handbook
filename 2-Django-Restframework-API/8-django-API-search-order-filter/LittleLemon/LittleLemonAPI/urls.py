from django.urls import path
from . import views

urlpatterns = [
    
    path('menu-items', views.menu_items),
    path('categories-items', views.category_item)

]