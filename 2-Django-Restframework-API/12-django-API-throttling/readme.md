Hedef = Throttle yani kısma, user veya anonim kişi request atarken işin dozunu kaçırmasın diye :)

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

```python
from rest_framework.throttling import AnonRateThrottle
```

``` python
@api_view()
@throttle_classes([AnonRateThrottle])
def throtthle_check(request):
    return Response({"message": "Succesful"})
```

Anonim kullanıcılar request atarken;

Günde 2 kere olarak ayarlı yani auth'suz 2 kere request atabilirsiniz.

``` python
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
),
'DEFAULT_THROTTLE_RATES' : { 
    'anon':'2/days',
    'user':'5/minute',
    'ten':'10/minute'
                           }
                 }
```

Authenticate kullanıcılar request atarken;

```python
@api_view()
@throttle_classes([UserRateThrottle])
#@throttle_classes([TenCallsPerMinute])
def throtthle_check_auth(request):
    return Response({"message": "message for the logged in users only"})

```

``` python
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
),
'DEFAULT_THROTTLE_RATES' : { 
    'anon':'2/days',
    'user':'5/minute',
    'ten':'10/minute'
                           }
                 }
```

* throttle.py

Custom throttle ayarı.

```python
from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'
```

* views.py

Comment-auth yeri değişti.

```python
@api_view()
#@throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute])
def throtthle_check_auth(request):
    return Response({"message": "message for the logged in users only"})

```
ten olarak tanımladığın TenCallsPerMinute class'ı üzerinden tanımlanabilmesi için aralık tanımla.

orn: dakikada 10 request

``` python
REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
),
'DEFAULT_THROTTLE_RATES' : { 
    'anon':'2/days',
    'user':'5/minute',
    'ten':'10/minute'
                           }
                 }
```


NOT: Requestleri atarken POSTMAN veya INSOMNIA gibi araçlar üzerinden yollayıznız.

docker attach thorottleauthcontainer (ctrl+c dediğinizde konteyner'ı stop edecektir boş bir terminal açıp izlemenizde fayda var.)

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t thorottlecontainer:0.0.1 .

docker run -p 8000:8000 -d --name thorottleauthcontainer thorottlecontainer:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

Not : Python 3.10.8 versiyonu kullanılmıştır.
