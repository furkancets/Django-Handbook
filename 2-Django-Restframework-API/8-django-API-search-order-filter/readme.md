Hedef = Search-Order-Filtering

* views.py

Değişiklikleri yaptığımız odaklanmamız gereken fonksiyon.

``` python

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

``` 

Konteyner'ı çalışır duruma getirdikten sonra kontrol edebileceğimiz bazı endpointler.


``` h

http://localhost:8000/api/menu-items?category=icecek

http://localhost:8000/api/menu-items?search=ada

http://localhost:8000/api/menu-items?order=price,inventory

``` 

NOT: Özellikle sqlite.db ile paylaşıyorum.

docker attach sofcontainer (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t restsof:0.0.1 .

docker run -p 8000:8000 -d --name sofcontainer restsof:0.0.1


Not : Python 3.10.8 versiyonu kullanılmıştır.

