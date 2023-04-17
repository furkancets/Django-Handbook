Hedef = Basit bir template sistemi yaratıp hakkında sayfası yazmak ve html dosyalarunı düzenlemek.

* models.py
Öncelikle models.py'dan başlanmalı burada kayıt altına alıcanacak veriler uygun formatta tanıtılmalı.

* admin.py
Bu tarafta yine models.py'da oluşturduğumuz Menu class'ını göreceksiniz.

* templates 
basictemplates/myproject'in altına templates isminde bir dosya oluşturuyoruz. .html dosyalarımızı burada tutacağız.

* settings.py
Burada TEMPLATES kısmında DIRS bölümünde templateleri sakladığımızı göstermemiz gerekir.

* about.html ve menu.html
Dosyalarını oluştururuz.

* views.py
views.py dosyasını .html render'larını alacak şekilde döndürüyoruz.

* static/img 
İstediğiniz bir fotoğraf atabilirsiniz.

* Not : Burada önemli olan html ve views file arasındaki ilişkiyi görebilmek.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t basictemplates:0.0.1 .

docker run -p 8000:8000 -d --name templatescontainer basictemplates:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it templatescontainer /bin/bash

cd myproject

* python manage.py createsuperuser

Not : Python 3.10.8 versiyonu kullanılmıştır.
