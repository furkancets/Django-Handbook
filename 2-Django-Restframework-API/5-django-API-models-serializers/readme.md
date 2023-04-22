Hedef = http://127.0.0.1:8000/api/menu-items/ 'i keşfetmek ve model seviyesinde serializer yazabilmek.

* models.py

Artık efektif bir şekilde model oluşturabiliyoruz.

* views.py

menu_items adında api_view() decorator'unu kullanan basit bir fonksiyon oluşturuyoruz.

```python
@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerilizer(items, many=True)
    return Response(serialized_item.data)
```
Her zaman ki gibi MenuItems'dan query'lerimizi çağırıyoruz.

MenuItem.objects.all() bu kod satırı diyor ki ; MenuItem adında models.py'da oluşturduğun objects yapısına git ve tüm kayıtları çağır.

Yani SQL dilinde  ``` select * from MenuItem; ```

Serilizers'da hazırladığımız methodlara göre data'yı direk fonksionun cevabı olarak döndürüyoruz.

* serializers.py

```python
class MenuItemSerilizer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock','price_after_tax']

    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
```

Örneğin inventory kelimesinin yerine stock kelimesini nasıl kullanacacağımızın bir örneği.

Veya vergi'den sonraki ücreti hesaplayabilmek için yeni bir fonksiyon ile bunu nasıl gerçekleştirebileceğimizin örneği.

Not: Bu örneği özellikle .db ile beraber paylaşacağım için her hangi bir POST methodu eklemedim. Hali hazırda veriler ile paylaşılmıştır.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t apiserializers:0.0.1 .

docker run -p 8000:8000 -d --name serializerscontainer apiserializers:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.

https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker