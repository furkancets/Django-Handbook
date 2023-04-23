Hedef =  Search-Order-Filtering-Pagination

* settings.py

django_filters ekledik.

ve

pip install django-filters(requiriments.txt'den geldiğinden dolayı ekstra bilgi olması adına ekledim)

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'LittleLemonDRF',
    'django_filters',
]
``` 

PAGE_SIZE değişkenini kurcalayıp bir sayfadaki kayıt sayısını istediğiniz gibi değiştirebilirsiniz.(Tabi canlıda performans kriterlerinizi lütfen göz önünde bulundurun.)

``` python

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [ 
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
        'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 3
}
``` 

* views.py

Değişiklikleri yaptığımız odaklanmamız gereken fonksiyon.

Bir önceki çalışmamızın temiz ve kolay hali.

``` 
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

``` 

Konteyner'ı çalışır duruma getirdikten sonra kontrol edebileceğimiz bazı endpointler.


Options'un yanında yeni filters isminde bir icon çıkmış olması lazım. Orayı keşfedebiliriz.


NOT: Özellikle sqlite.db ile paylaşıyorum.

docker attach sofpcontainer (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t sofpcontainer:0.0.1 .

docker run -p 8000:8000 -d --name sofp sofpcontainer:0.0.1


Not : Python 3.10.8 versiyonu kullanılmıştır.

