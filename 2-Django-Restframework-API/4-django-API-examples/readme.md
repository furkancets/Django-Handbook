Hedef = http://127.0.0.1:8000/api/menu-items/ gittiğiniz'de sağ üst köşede DjDT simgesine bakıp bunu keşfetmek.

* models.py

Artık efektif bir şekilde model oluşturabiliyoruz.

* views.py

API'ın nasıl görüneceğini viewlar sayesinde oluşturduğumuzu hatırlıyoruz.

Burada özellikle bir class'ı buraya getirdim altına bir iki not ekleyelim.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilizer

MenuItem.objects.all() bu kod satırı diyor ki ; MenuItem adında models.py'da oluşturduğun objects yapısına git ve tüm kayıtları çağır.

Yani SQL dilinde ' select * from MenuItem; '

Öncelikle generics rest_framework'ün içinden gelen bir kütüphane ve aşağıdaki işlemleri yapabiliyor;

| Generic view class | Supported method | Purpose |
| --- | --- | --- |
| CreateAPIView | POST | Create a new resource |
| ListAPIView | GET | Display resource collection |
| RetrieveAPIView | GET | Display a single resource |
| DestroyAPIView | DELETE | Delete a single resource |
| UpdateAPIView | PUT and PATCH | Replace or partially update a single resource |
| ListCreateAPIView | GET, POST | Display resource collection and create a new resource |
| RetrieveUpdateAPIView | GET, PUT, PATCH | Display a single resource and replace or partially update it |
| RetrieveDestroyAPIView | GET, DELETE | Display a single resource and delete it |
| RetrieveUpdateDestroyAPIView | GET, PUT, PATCH, DELETE | Display, replace or update and delete a single resource |


* serializers.py

Burada api tarafında hangi kolonları gösterip göstermeyeceğimizi belirleyebiliriz.

Örneğin fields kısmında id sildiğinizde id bilgisi görülmeyecektir.

Değişikliği denedikten sonra build almayını unutma ve 0.0.1 tag'inide daha önce build aldıysan 0.0.1 versiyonu ile ilerlemeyi unutma !

Serializers'da ileriki örneklerdede çeşitli işlemler validasyon örnekleri yapacağız.


Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t apiexample:0.0.1 .

docker run -p 8000:8000 -d --name examplecontainer apiexample:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.

https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker