Hedef = djoser kütüphanesiyle kolay auth ayarları.

* settings.py

settings'in içine gerekli ayarları ekliyoruz. Bu işlemi aynı zamanda E-mail based'de yapabiliriz. 

``` python
DJOSER = {
    
    "USER_ID_FIELD": "username"
    
}
```

* urls.py (project-level)

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("LittleLemonAPI.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
```

http://localhost:8000/auth/ ' un altında kullanabileceğiniz bazı endpointler oluşmuştur.

Endpoint'lerin detaylı bilgilerine buradan https://djoser.readthedocs.io/en/latest/getting_started.html ulaşabilirsiniz.

Örnek url kullanımları

http://127.0.0.1:8000/auth/token/login

FORM URL Encoded olduğundan emin olunuz.

aşağıdaki parametrelerini giriniz ve POST methodu ile yollayınız token geri dönecektir.

username:admin

password:admin

NOT: Lütfen tek tek POST veya GET ediniz ve değişiklikleri gözlemleyiniz.

docker attach djosercontainer (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t djoserauth:0.0.1 .

docker run -p 8000:8000 -d --name djosercontainer djoserauth:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.

https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker
