Hedef = djoser kütüphanesiyle kolay auth ayarları.

* settings.py

settings'in içine gerekli ayarları ekliyoruz. Bu işlemi aynı zamanda E-mail based'de yapabiliriz. 

```python
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework_simplejwt.authentication.JWTAuthentication',
),
'DEFAULT_THROTTLE_RATES' : { 
    'anon':'2/days',
    'user':'5/minute',
    'ten':'10/minute',
                           }
                 }


DJOSER = {
    
    "USER_ID_FIELD": "username"
    
}


SIMPLE_JWT = {
    
    'ACCES_TOKEN_LIFETIME': timedelta(minutes=5)
}

```

* urls.py (project-level)

```python

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("LittleLemonAPI.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("api/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/token/refresh", TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    
]

```

* username ve pass ile refresh ve acces token'i alma.
 
```HTTP

POST /api/token/ HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: 127.0.0.1:8000
Content-Length: 33

username=selami&password=kermit12

```

* Mesaja alınan token ile erişebilme.

```HTTP
GET /api/secret HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyNDQyNzQ2LCJpYXQiOjE2ODI0NDE5NzMsImp0aSI6ImQxOGVlMWFlMzM3YjRjZmJhMjc5M2ViNmYwNDFmNWRkIiwidXNlcl9pZCI6Mn0.rBGZBKkdCcrVj2pdEAQIfH6gpWc3ojhrfwtb4ZGTjzg
Host: 127.0.0.1:8000

```
* refresh token'ı yenileme.

```HTTP
POST /api/token/refresh HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: 127.0.0.1:8000
Content-Length: 237

refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjUyODM3MywiaWF0IjoxNjgyNDQxOTczLCJqdGkiOiI0OTQ0NGJjYTEwN2M0YzYxOTY4MDUxNTNmOWVmNGUyNyIsInVzZXJfaWQiOjJ9.ENC8wOuBa-XCFy7oM80jPXiW6alWZJjLeG3_RN2JK3E

```
* token'ı blackliste atama.

```HTTP

POST /api/token/blacklist/ HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: 127.0.0.1:8000
Content-Length: 237

refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MjUyODM3MywiaWF0IjoxNjgyNDQxOTczLCJqdGkiOiI0OTQ0NGJjYTEwN2M0YzYxOTY4MDUxNTNmOWVmNGUyNyIsInVzZXJfaWQiOjJ9.ENC8wOuBa-XCFy7oM80jPXiW6alWZJjLeG3_RN2JK3E
```

NOT: Lütfen tek tek POST veya GET ediniz ve değişiklikleri gözlemleyiniz.

docker attach jwtauth (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t jwtauth:0.0.1 .

docker run -p 8000:8000 -d --name jwtcontainer jwtauth:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.

https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker
