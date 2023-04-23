Hedef = http://127.0.0.1:8000/api/menu-items/ 'i keşfetmek ve model seviyesinde serializer yazabilmek.

* models.py

Artık efektif bir şekilde model oluşturabiliyoruz.

Category class'ını modelimize dahil ediyoruz. Eklenen yerin bir relation'nunu hali hazırda bulunan menu-items'a bağlıyoruz. 

* serializers.py

CategorySerializers'ı ekliyoruz. Model tarafında yarattığımız Category class'ını serialize ediyoruz.(Fields kısmından eklistmek veya karşıya göstermek istemediğiniz bir yer varsa silebilirsiniz veya MenuItemSerilizer'da yaptığımız gizi özel kurallara tabi tutabilirsiniz.)

* views.py

menu_items ve category adında api_view() decorator'unu kullanan basit bir fonksiyon oluşturuyoruz.

Bu sefer GET ve POST methodlarını kullanağımızı decoratore tanımlıyoruz.

POST ve GET işlemlerinde nasıl davranacağınız if conditionsları ile belirliyoruz.

Dikkat edilmesi gereken yer menu_items'ı oluştururken ``` items = MenuItem.objects.select_related('category').all() ``` kısmını kategorik bilgi içermesini mecburi kılmak.

---
Manuel olarak veri ekleyeceğiz. İlk önce category kısmını tanımlamak zorundayız çünkü FOREIGN KEY olarak belirlediğimiz Category tanımı olmadan POST edersek Foreign key constraint hatası fırlatacaktır.

Örnekler;

NOT: Lütfen tek tek POST ediniz ve değişiklikleri gözlemleyiniz.

docker attach relationcontainer (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

* Category;
```
{
        "slug": "gida",
        "title": "icecek"
}
```

```
{
        "slug": "gida",
        "title": "anayemek"
}
```

```
{
        "slug": "gida",
        "title": "tatli"
}
```

* Menu-items;
```
{
"title": "ayran",
"price": "8.00",
"stock": 20,
"category_id": 1
}
```
```
{
"title": "adana-kebap",
"price": "75.00",
"stock": 1,
"category_id":2
}
```
```
{
"title": “künefe”,
"price": “55.00",
"stock": 2,
"category_id”:3
}
```
```
{
"title": "künefe",
"price": "55.00",
"stock": 2,
"category_id":3
}
```

---

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t relationserializers:0.0.1 .

docker run -p 8000:8000 -d --name relationcontainer relationserializers:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.

https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker