Hedef = User based erişimler sayseinde veri ulaşımı kısıtlaması veya hareket alanı kısıtlaması.

* http://127.0.0.1:8000/admin/

user: admin
pass: admin

* http://127.0.0.1:8000/admin/auth/group/

İlk adımda user group oluşturdum.İsmi Manager.

* http://127.0.0.1:8000/admin/auth/user/

Userları oluşturdum Selami ve Ayhan

* http://127.0.0.1:8000/admin/auth/user/2/change/

Selami'yi oluşturduğum Manager grubuna ekledim.

* http://127.0.0.1:8000/admin/auth/user/3/change/

Ayhan'ı eklemedim.

* views.py

``` python
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({"message": "Only Manager Should see this."})
    else:
        return Response({"message": "You are not authorized"}, 403)
```

Bir önceki örnekte olduğu gibi POST ``` http://127.0.0.1:8000/api/api-token-auth ``` methoduyla her bir kullanıcıya token al.(Form url encoded olduğuna emin ol.) 

```
username: selami
password: kermit12
```

```
username: ayhan
password: kermit12
```

Bir önceki örnekte olduğu gibi GET ``` http://127.0.0.1:8000/api/manager-view/ ``` methoduyla her bir kullanıcının hangi method ile hangi mesajı aldığına dikkat et. Fonksiyonda yazdığın condition'a uyuyor mu ?

```
Ayhan
token: c279c4e3ff150edc3f8c00686a708226f5a2d0ad

Selami
token: 56f34cf5cc46f72c3256e7dc778f4dd1b6084e1a
```

NOT: Requestleri atarken POSTMAN veya INSOMNIA gibi araçlar üzerinden yollayıznız.

docker attach userauthcontainer (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t userauth:0.0.1 .

docker run -p 8000:8000 -d --name userauthcontainer userauth:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.
