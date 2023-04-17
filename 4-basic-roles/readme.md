Hedef = Basit bir rol atamayı anlamak.

* models.py
Öncelikle models.py'dan başlanmalı burada kayıt altına alıcanacak veriler uygun formatta tanıtılmalı.

* admin.py
Bu tarafta yine models.py'da oluşturduğumuz Employees class'ını göreceksiniz.

* settings.py

Aşağıdaki bölüme bunu eklediğinizde emin olun.

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',

* Bu bölümde herhangi bir views.py, .html, veya url ayarlamadan devam ediyoruz. Bundan dolayı Django'yu ayağı kaldırdığınızda karşınıza çıkan default görüntü gelecektir.

Uygulamayı çalıştırmak için dockerize etmeniz yeterli

docker build -t basicroles:0.0.1 .

docker run -p 8000:8000 -d --name rolescontainer basicroles:0.0.1

Eğer admin tarafından kontol etmek istiyorsak container içinde girip;

docker exec -it rolescontainer /bin/bash

cd myproject

* python manage.py createsuperuser

http://127.0.0.1:8000/admin/auth/user/2/change/

User'ı oluşturduktan sonra yukarıdaki adrese gidip permissions bölümündeki yetkleri değiştirerek oluşturduğumuz "Employeess" class'ına log girip girememe durumlarınızı kontrol edin.
