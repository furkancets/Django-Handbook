from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    path('menu-items/', views.menu_items),
    path('categories-items/', views.category_item),
    #path('menu-items/<int:pk>', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth', obtain_auth_token)

]